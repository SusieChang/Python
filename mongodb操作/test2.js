var mongoose = require('mongoose');
var xlsx = require('node-xlsx');
mongoose.connect("mongodb://sysu:sysu2018@ds113693.mlab.com:13693/geokg",{ useNewUrlParser: true });
var db = mongoose.connection;
db.on('error', console.error.bind(console, '数据库连接失败:'));
db.once('open', function() {
  console.log('数据库已连接');
});

const buildingSchema = new mongoose.Schema({
    name : {type : String},
    types: {type : Array},
    materials: {type : Array},
    built_year: {type : String},
    address: {type : String},
    belong_to: {type: mongoose.Schema.Types.ObjectId},
    description: {type : String},
    id: {type: Number}
} ,{versionKey: false});

const districtSchema = new mongoose.Schema({
    // _id : {type : mongoose.Schema.Types.ObjectId},
    id: {type : Number},
    name : {type : String},
    belong_to: {type: mongoose.Schema.Types.ObjectId}
},{versionKey:false});

const BuildingModel = mongoose.model('building', buildingSchema, 'building');
const DistrictModel = mongoose.model('district', districtSchema, 'district');
var indexs = {};
var doc = {};
async function setBuilding() {
	var buildingExcel = xlsx.parse('E:/资料/大三下/实训/广府建筑表格/building.xls')[0];
	var buildingArray = [];
	var buildingDoc = [];
	for(var rowId in buildingExcel['data']) {
		if(rowId == 0) continue;
		var row = buildingExcel['data'][rowId];
		buildingArray.push(row);
	}
	for(let i = 0; i < buildingArray.length; i++) {
		var line = buildingArray[i];
		doc[line[1]] = line[6];
	}
	var criteria = {};
	var fields = {id: 1, _id: 1};
	var options = {};
	
	await DistrictModel.find(criteria, fields, options, function (error, result) {
		if(error) {
			console.log(error);
		} else {
			console.log('get district data');
			for(let i = 0; i < result.length; i++) {
				indexs[result[i]["id"]] = result[i]["_id"];
			}
			for(let key in doc) {
				let id = doc[key];
				doc[key] = indexs[id];
				BuildingModel.findOne({name:key},function (error, result) {
					result["belong_to"] = doc[key];
					result.save();
				});
			}
			console.log(doc);
		}
	});
}

setBuilding();