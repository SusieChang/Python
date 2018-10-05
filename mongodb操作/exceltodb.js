var mongoose = require('mongoose');
var xlsx = require('node-xlsx');

mongoose.connection.on('connected', function() {
    // Hack the database back to the right one, because when using mongodb+srv as protocol.
    if (mongoose.connection.client.s.url.startsWith('mongodb+srv')) {
        mongoose.connection.db = mongoose.connection.client.db('geokg');
    }
    console.log('Connection to MongoDB established.')
});
mongoose.connect("mongodb+srv://sysu:sysu2018@cluster0-gmjko.mongodb.net/geokg",{ useNewUrlParser: true });
var db = mongoose.connection;
db.on('error', console.error.bind(console, '数据库连接失败:'));
db.once('open', function() {
  console.log('数据库已连接');
});


//Model
const regionSchema = new mongoose.Schema({
    id: {type : Number},
    name : {type : String}
});

const districtSchema = new mongoose.Schema({
    // _id : {type : mongoose.Schema.Types.ObjectId},
    id: {type : Number},
    name : {type : String},
    belong_to: {type: mongoose.Schema.Types.ObjectId}
});

const buildingSchema = new mongoose.Schema({
    // _id : {type : mongoose.Schema.Types.ObjectId},
    id: {type : Number},
    name : {type : String},
    type: {type : String},
    material: {type : String},
    built_year: {type : String},
    address: {type : String},
    belong_to: {type: mongoose.Schema.Types.ObjectId},
    description: {type : String}
});

const RegionModel = mongoose.model('region', regionSchema, 'region');
const DistrictModel = mongoose.model('district', districtSchema, 'district');
const BuildingModel = mongoose.model('building', buildingSchema, 'building');

//region
var regionExcel = xlsx.parse('E:/资料/大三下/实训/广府建筑表格/region.xls')[0];
var regionArray = [];
var regionDoc = [];

for(var rowId in regionExcel['data']) {
	if(rowId == 0) continue;
	var row = regionExcel['data'][rowId];
	regionArray.push(row);
}

for(var i = 0; i < regionArray.length; i++) {
	var line = regionArray[i];
	var doc = {};
	doc["id"] = line[0];
	doc["name"] = line[1];
	regionDoc.push(doc);
}
console.log(regionDoc);

for(var i = 0; i < regionDoc.length; i++) {
	RegionModel.create(regionDoc[i], function (error) {
	if(error) {
		console.log(error);
	} else {
		console.log('save ok');
	}
});
}

//district
var districtExcel = xlsx.parse('E:/资料/大三下/实训/广府建筑表格/district.xls')[0];
var districtArray = [];
var districtDoc = [];

for(var rowId in districtExcel['data']) {
	if(rowId == 0) continue;
	var row = districtExcel['data'][rowId];
	districtArray.push(row);
}

for(var i = 0; i < districtArray.length; i++) {
	var line = districtArray[i];
	var doc = {};
	doc["id"] = line[0];
	doc["name"] = line[1];
	doc["belong_to"] = line[2];
	districtDoc.push(doc);
}

function setDistrict(i) {
	setTimeout(function (argument) {
	var criteria = {id: districtDoc[i]['belong_to']};
	var fields = {_id: 1};
	var options = {};
	var region_id;
	RegionModel.find(criteria, fields, options, function (error, result) {
		if(error) {
			console.log(error);
		} else {
			region_id = result[0]["_id"];
			districtDoc[i]['belong_to'] = region_id;
			console.log(districtDoc[i]);
				DistrictModel.create(districtDoc[i], function (error) {
					if(error) {
						console.log(error);
					} else {
						console.log('save ok');
					}
				});
			}
			db.close();
		});
	}, 1000);
}

for(var i = 0; i < districtDoc.length; i++) {
	setDistrict(i);
}

//building
var buildingExcel = xlsx.parse('E:/资料/大三下/实训/广府建筑表格/building.xls')[0];
var buildingArray = [];
var buildingDoc = [];

for(var rowId in buildingExcel['data']) {
	if(rowId == 0) continue;
	var row = buildingExcel['data'][rowId];
	buildingArray.push(row);
}

for(var i = 0; i < buildingArray.length; i++) {
	var line = buildingArray[i];
	var doc = {};
	doc["id"] = line[0];
	doc["name"] = line[1];
	doc["type"] = line[2];
	doc["material"] = line[3];
	doc["built_year"] = line[4];
	doc["address"] = line[5];
	doc["belong_to"] = line[6];
	doc["description"] = line[7];
	buildingDoc.push(doc);
}

function setBuilding(i) {
	setTimeout(function (argument) {
	var criteria = {id: buildingDoc[i]['belong_to']};
	var fields = {_id: 1};
	var options = {};
	var region_id;
	DistrictModel.find(criteria, fields, options, function (error, result) {
		if(error) {
			console.log(error);
		} else {
			district_id = result[0]["_id"];
			buildingDoc[i]['belong_to'] = district_id;
			console.log(buildingDoc[i]);
				BuildingModel.create(buildingDoc[i], function (error) {
					if(error) {
						console.log(error);
					} else {
						console.log('save ok');
					}
				});
			}
		});
	}, 1000);
}

for(var i = 0; i < buildingDoc.length; i++) {
	setBuilding(i);
}
