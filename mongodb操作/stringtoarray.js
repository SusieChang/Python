var mongoose = require('mongoose');
// mongoose.connection.on('connected', function() {
//     // Hack the database back to the right one, because when using mongodb+srv as protocol.
//     if (mongoose.connection.client.s.url.startsWith('mongodb+srv')) {
//         mongoose.connection.db = mongoose.connection.client.db('geokg');
//     }
//     console.log('Connection to MongoDB established.')
// });
//mongoose.connect("mongodb+srv://sysu:sysu2018@cluster0-gmjko.mongodb.net/geokg",{ useNewUrlParser: true });
mongoose.connect("mongodb://sysu:sysu2018@ds113693.mlab.com:13693/geokg",{ useNewUrlParser: true });
var db = mongoose.connection;
db.on('error', console.error.bind(console, '数据库连接失败:'));
db.once('open', function() {
  console.log('数据库已连接');
});

const buildingsSchema = new mongoose.Schema({
    name : {type : String},
    types: {type : Array},
    materials: {type : Array},
    built_year: {type : String},
    address: {type : String},
    belong_to: {type: mongoose.Schema.Types.ObjectId},
    description: {type : String}
}, {versionKey: false});

const buildingSchema = new mongoose.Schema({
    name : {type : String},
    types: {type : String},
    materials: {type : String},
    built_year: {type : String},
    address: {type : String},
    belong_to: {type: mongoose.Schema.Types.ObjectId},
    description: {type : String}
} ,{versionKey: false});

const BuildingModel = mongoose.model('building', buildingSchema, 'building');
const BuildingsModel = mongoose.model('buildings', buildingsSchema, 'buildings');

var buildingDoc = [];
var buildingsDoc = [];

function stringToArray() {
	BuildingModel.find({}, function(error, result) {
		if(error) {
			console.log(error);
		} else {
			console.log('get building');
			buildingDoc = result;
			console.log(result.length);
		}
	});	
}

stringToArray();

setTimeout(function (argument) {
	for(let i = 0; i < buildingDoc.length; i++) {
		var doc = {};
		doc["name"] = buildingDoc[i]["name"];
		doc["built_year"] = buildingDoc[i]["built_year"];
		doc["description"] = buildingDoc[i]["description"];
		doc["address"] = buildingDoc[i]["address"];
		var types = buildingDoc[i]["types"] || "";
		var arr = types.split('、');
		doc["types"] = [];
		for(let i = 0; i < arr.length; i++) {
			doc["types"].push(arr[i]);
		}
		var materials = buildingDoc[i]["materials"] || "";
		var arr = materials.split('、');
		doc["materials"] = [];
		for(let i = 0; i < arr.length; i++) {
			doc["materials"].push(arr[i]);
		}
		buildingsDoc.push(doc);
		console.log(doc);
	}
	setTimeout(function (argument) {
		/* body... */
		BuildingsModel.insertMany(buildingsDoc, function (error) {
		if(error) {
			console.log(error);
		} else {
			console.log('save success');
		}
		db.close();
	});
	}, 1000);
}, 3000);