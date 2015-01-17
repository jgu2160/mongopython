use test
db.smallzips.aggregate([
	{$group:{_id:{city:"$city",state:"$state"},pop:{$sum:"$pop"}}},
	{$match:{$and:[{"_id.state":{$in:["NY","CA"]}},{pop:{$gt:25000}}]}},
	{$group:{_id:null,pop_avg:{$avg:"$pop"}}}
])
