use test
db.zips.aggregate([
    {$project:{pop:1,first_char:{$substr : ["$city",0,1]}}},
    {$match:{first_char:{$in:["0","1","2","3","4","5","6","7","8","9"]}}},
    {$group:{_id:null,total:{$sum:"$pop"}}}
    ])


db.zips.aggregate([
	{$project:{pop:1,first_char:{$substr:["city",0,1]}}},
	{$match:{first_char:{$in:["0"]}}},
	{$group:{_id:null,total:{$sum:"$pop"}}}
	])
