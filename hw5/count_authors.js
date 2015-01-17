use blog
db.posts.aggregate([
	{$unwind:"$comments"},
	{$group:{_id:"$comments.author",posts_count:{$sum:1}}},
	{$sort:{posts_count:-1}}
	])