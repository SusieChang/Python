var mongoose = require('mongoose');
// mongoose.connection.on('connected', function() {
//     // Hack the database back to the right one, because when using mongodb+srv as protocol.
//     if (mongoose.connection.client.s.url.startsWith('mongodb+srv')) {
//         mongoose.connection.db = mongoose.connection.client.db('geokg');
//     }
//     console.log('Connection to MongoDB established.')
// });
//mongoose.connect("mongodb+srv://sysu:sysu2018@cluster0-gmjko.mongodb.net/geokg",{ useNewUrlParser: true });
mongoose.connect("mongodb://47.106.173.16:27017/GeoKG",{ useNewUrlParser: true });
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
    district: {type: String},
    region: {type: String},
    location: {type: Object}
} ,{versionKey: false});

const typeSchema = new mongoose.Schema({
    name : {type : String}
} ,{versionKey: false});

const materialSchema = new mongoose.Schema({
    name : {type : String}
} ,{versionKey: false});

const districtSchema = new mongoose.Schema({
    name : {type : String},
    belong_to: {type: String}
} ,{versionKey: false});
const regionSchema = new mongoose.Schema({
    name : {type : String},
} ,{versionKey: false});


const BuildingModel = mongoose.model('building', buildingSchema, 'building');
const BuildingsModel = mongoose.model('buildings', buildingSchema, 'buildings');
const TypeModel = mongoose.model('type', typeSchema, 'type');
const MaterialModel = mongoose.model('material', materialSchema, 'material');
const DistrictModel = mongoose.model('district', districtSchema, 'district');
const DistrictsModel = mongoose.model('districts', districtSchema, 'districts');
const RegionModel = mongoose.model('region', regionSchema, 'region');
var materials = {};
var types = {};
var buildings = [];
var district = {};
var regions = {};
var districts = [];
	var mapData = [
      {
        "name": "开平碉楼",
        "location": {
          "lat": 22.376136,
          "lng": 112.586459
        }
      },
      {
        "name": "陶陶居",
        "location": {
          "lat": 23.119175,
          "lng": 113.248942
        }
      },
      {
        "name": "广州酒家",
        "location": {
          "lat": 23.083308,
          "lng": 113.234994
        }
      },
      {
        "name": "陈氏书院(陈家祠)",
        "location": {
          "lat": 23.132712,
          "lng": 113.251508
        }
      },
      {
        "name": "莲香楼",
        "location": {
          "lat": 23.119387,
          "lng": 113.251609
        }
      },
      {
        "name": "西关大屋",
        "location": {
          "lat": 23.124185,
          "lng": 113.242876
        }
      },
      {
        "name": "海山仙馆",
        "location": {
          "lat": 23.12873,
          "lng": 113.239187
        }
      },
      {
        "name": "东山住宅群",
        "location": {
          "lat": 23.123015,
          "lng": 113.304595
        }
      },
      {
        "name": "余荫山房(余荫园)",
        "location": {
          "lat": 23.018073,
          "lng": 113.401684
        }
      },
      {
        "name": "卢家大屋",
        "location": {
          "lat": 22.19737,
          "lng": 113.552811
        }
      },
      {
        "name": "可园",
        "location": {
          "lat": 23.049565,
          "lng": 113.750501
        }
      },
      {
        "name": "梁园",
        "location": {
          "lat": 23.044003,
          "lng": 113.120253
        }
      },
      {
        "name": "清晖园",
        "location": {
          "lat": 22.841731,
          "lng": 113.26195
        }
      },
      {
        "name": "孙中山故居",
        "location": {
          "lat": 22.447738,
          "lng": 113.535053
        }
      },
      {
        "name": "赤坎骑楼街",
        "location": {
          "lat": 22.32588,
          "lng": 112.59098
        }
      },
      {
        "name": "关族图书馆",
        "location": {
          "lat": 22.325528,
          "lng": 112.591676
        }
      },
      {
        "name": "关族图书馆",
        "location": {
          "lat": 22.325528,
          "lng": 112.591676
        }
      },
      {
        "name": "立园",
        "location": {
          "lat": 22.356409,
          "lng": 112.573527
        }
      },
      {
        "name": "风采堂",
        "location": {
          "lat": 22.35904,
          "lng": 112.688139
        }
      },
      {
        "name": "天禄楼",
        "location": {
          "lat": 22.292971,
          "lng": 112.575864
        }
      },
      {
        "name": "骏庐",
        "location": {
          "lat": 22.290227,
          "lng": 112.575619
        }
      },
      {
        "name": "庆林村闸楼",
        "location": {
          "lat": 22.679574,
          "lng": 113.138998
        }
      },
      {
        "name": "林庐",
        "location": {
          "lat": 22.288839,
          "lng": 112.576302
        }
      },
      {
        "name": "云幻楼",
        "location": {
          "lat": 22.380448,
          "lng": 112.585339
        }
      },
      {
        "name": "铭石楼",
        "location": {
          "lat": 22.380391,
          "lng": 112.585707
        }
      },
      {
        "name": "澜生居庐",
        "location": {
          "lat": 22.376471,
          "lng": 112.58665
        }
      },
      {
        "name": "方氏灯楼",
        "location": {
          "lat": 22.376471,
          "lng": 112.58600
        }
      },
      {
        "name": "养闲别墅",
        "location": {
          "lat": 22.380386,
          "lng": 112.58478
        }
      },
      {
        "name": "竹林楼",
        "location": {
          "lat": 22.38064,
          "lng": 112.586129
        }
      },
      {
        "name": "叶生居庐",
        "location": {
          "lat": 22.380172,
          "lng": 112.585815
        }
      },
      {
        "name": "瑞石楼",
        "location": {
          "lat": 22.264736,
          "lng": 112.532599
        }
      },
      {
        "name": "莼园",
        "location": {
          "lat": 23.665594,
          "lng": 116.656665
        }
      },
      {
        "name": "资政第",
        "location": {
          "lat": 23.481408,
          "lng": 116.657478
        }
      },
      {
        "name": "香园",
        "location": {
          "lat": 23.360822,
          "lng": 116.689871
        }
      },
      {
        "name": "陈慈黉故居（郎中第）",
        "location": {
          "lat": 23.572697,
          "lng": 116.751738
        }
      },
      {
        "name": "陈慈黉故居（三庐）",
        "location": {
          "lat": 23.572690,
          "lng": 116.751730
        }
      },
      {
        "name": "陈慈黉故居（寿康里）",
        "location": {
          "lat": 23.572697,
          "lng": 116.751750
        }
      },
      {
        "name": "西塘",
        "location": {
          "lat": 23.573892,
          "lng": 116.829805
        }
      },
      {
        "name": "运际春光宅",
        "location": {
          "lat": 23.576458,
          "lng": 116.828791
        }
      },
      {
        "name": "磊园（耐轩）",
        "location": {
          "lat": 23.263896,
          "lng": 116.605613
        }
      },
      {
        "name": "林园",
        "location": {
          "lat": 23.265156,
          "lng": 116.619465
        }
      },
      {
        "name": "梅祖家祠",
        "location": {
          "lat": 23.397502,
          "lng": 116.437642
        }
      },
      {
        "name": "西园",
        "location": {
          "lat": 23.296144,
          "lng": 116.461039
        }
      },
      {
        "name": "小可楼",
        "location": {
          "lat": 23.280103,
          "lng": 116.479492
        }
      },
      {
        "name": "海源楼",
        "location": {
          "lat": 24.304337,
          "lng": 116.777848
        }
      },
      {
        "name": "肇庆楼",
        "location": {
          "lat": 24.299177,
          "lng": 116.782232
        }
      },
      {
        "name": "荣禄第",
        "location": {
          "lat": 24.284376,
          "lng": 116.290547
        }
      },
      {
        "name": "先勤楼",
        "location": {
          "lat": 24.284376,
          "lng": 116.109909
        }
      },
      {
        "name": "济济楼",
        "location": {
          "lat": 24.278246,
          "lng": 116.091679
        }
      },
      {
        "name": "棣华居",
        "location": {
          "lat": 23.88364,
          "lng": 115.779986
        }
      },
      {
        "name": "联芳楼",
        "location": {
          "lat": 24.304988,
          "lng": 116.240487
        }
      },
      {
        "name": "万秋楼",
        "location": {
          "lat": 24.287564,
          "lng": 116.108456
        }
      },
      {
        "name": "南华又庐",
        "location": {
          "lat": 24.274586,
          "lng": 115.984322
        }
      },
      {
        "name": "全凤楼",
        "location": {
          "lat": 24.373719,
          "lng": 116.067252
        }
      },
      {
        "name": "卓府",
        "location": {
          "lat": 23.676936,
          "lng": 116.654735
        }
      },
      {
        "name": "人境庐",
        "location": {
          "lat": 24.316726,
          "lng": 116.136563
        }
      },
      {
        "name": "湛庐",
        "location": {
          "lat": 22.379595,
          "lng": 112.586062
        }
      },
      {
        "name": "琅琊世家",
        "location": {
          "lat": 23.574078,
          "lng": 116.826197
        }
      },
      {
        "name": "联辉楼",
        "location": {
          "lat": 24.370824,
          "lng": 116.069436
        }
      }
    ];

function change() {

	for(let i = 0; i < mapData.length; i++) {
		let name = mapData[i]["name"];
		let location = mapData[i]["location"];
		BuildingsModel.updateOne({"name": name},{$set: {"location": location}},function(err, res){
			if(err) {
				console.log(err);
			}
		})
	}
};

setTimeout(change, 1000);
