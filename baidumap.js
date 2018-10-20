var http = require('http');
var queryString = require('querystring');
var mongoose = require('mongoose');

mongoose.Promise = global.Promise;
mongoose.connect("mongodb://sysu:sysu2018@ds113693.mlab.com:13693/geokg",{ useNewUrlParser: true });
var db = mongoose.connection;
db.on('error', console.error.bind(console, '数据库连接失败:'));
db.once('open', function() {
  console.log('数据库已连接');
});

const buildingSchema = new mongoose.Schema({
    // _id : {type : mongoose.Schema.Types.ObjectId},
    id: {type : Number},
    name : {type : String},
    types: {type : String},
    materials: {type : String},
    built_year: {type : String},
    address: {type : String},
    belong_to: {type: mongoose.Schema.Types.ObjectId},
    description: {type : String}
});

const districtSchema = new mongoose.Schema({
    // _id : {type : mongoose.Schema.Types.ObjectId},
    id: {type : Number},
    name : {type : String},
    belong_to: {type: mongoose.Schema.Types.ObjectId}
});

const DistrictModel = mongoose.model('district', districtSchema, 'district');
const BuildingModel = mongoose.model('building', buildingSchema, 'building');

async function getLocationData (name, region) {
	var data = {
	'query':name,
	'region':region,
	'city_limit':true,
	'scope':1,
	'page_size':20,
	'output':'json',
	'ak':'agIYcxFrxnd5BKUZMqomPyCVUTWCq2pm' //GET请求
	}
	var content=queryString.stringify(data);
	var options={
		hostname : "api.map.baidu.com",
		path:'/place/v2/search?'+content,
		method:'GET'
	}
	var myresult = {};
	var request = await http.request(options,function(response){
		response.setEncoding('utf-8');
		response.on('data',function(result){
			console.log('success');
			setTimeout(function () {
				myresult = result;
			}, 200);
		});
		response.on('end',function(){
			console.log('end');
		});
	  })
	request.on('error',function(err){
	      console.error(err);
	});
	request.end();
	return new Promise(function (resolve, reject) {
		setTimeout(function () {
			resolve(myresult);
		}, 2500);
	});
}

async function storeLocation() {
	let data = await getLocationData("梅江区城北镇干光村", "梅州");
	console.log(data);
	// let buildings = await BuildingModel.find().exec();
	// for(let i = 0; i < buildings.length; i++) {
	// 	let district = await DistrictModel.findOne({"_id": buildings[i]["belong_to"]}, {"name": 1}, {}).exec();
	// 	// console.log(district["name"]);
	// 	setTimeout(async function () {
	// 		console.log([buildings[i]["name"], district["name"]]);
	// 		let data = await getLocationData(buildings[i]["name"], district["name"]);
	// 		if(data && data.result) {
	// 			console.log(buildings[i]["name"]);
	// 			// console.log(data);
	// 		}
	// 	}, 3000);
	// }
}

storeLocation();

		