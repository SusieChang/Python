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

const buildingSchema = new mongoose.Schema({
    name : {type : String},
    types: {type : Array},
    materials: {type : Array},
    built_year: {type : String},
    address: {type : String},
    belong_to: {type: mongoose.Schema.Types.ObjectId},
    description: {type : String}
} ,{versionKey: false});

const typeSchema = new mongoose.Schema({
    name : {type : String}
} ,{versionKey: false});

const materialSchema = new mongoose.Schema({
    name : {type : String}
} ,{versionKey: false});

const BuildingModel = mongoose.model('building', buildingSchema, 'building');
const BuildingsModel = mongoose.model('buildings', buildingSchema, 'buildings');
const TypeModel = mongoose.model('type', typeSchema, 'type');
const MaterialModel = mongoose.model('material', materialSchema, 'material');

var materials = {};
var types = {};
var buildings = [];

function nameToObjectId (argument) {
	TypeModel.find({}, function (error, result) {
		if(error) {
			console.log(error);
		} else {
			for(let i = 0; i < result.length; i++) {
				types[result[i]["name"]] = result[i]["_id"];
			}
			console.log(types);
		}
	});
	MaterialModel.find({}, function (error, result) {
		if(error) {
			console.log(error);
		} else {
			for(let i = 0; i < result.length; i++) {
				materials[result[i]["name"]] = result[i]["_id"];
			}
			console.log(materials);
		}
	});
}

nameToObjectId();

setTimeout(function (argument) {
	BuildingModel.find({}, function (error, result) {
		if(error) {
			console.log(error);
		} else {
			for(let i = 0; i < result.length; i++) {
				buildings.push(result[i]);
				for(let j = 0; j < buildings[i]["types"].length; j++) {
					buildings[i]["types"][j] = types[buildings[i]["types"][j]];
				}
				for(let j = 0; j < buildings[i]["materials"].length; j++) {
					buildings[i]["materials"][j] = materials[buildings[i]["materials"][j]];
				}
			}
		}
	});

	setTimeout(function () {
		BuildingsModel.insertMany(buildings, function (error) {
			if(error) {
				console.log(error);
			} else {
				console.log('save ok');
			}
			db.close();
		});
	}, 1000);

}, 2000);