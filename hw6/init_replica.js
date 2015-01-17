


config = { _id: "m101", members:[
          { _id : 0, host : "Jeffreys-MacBook-Pro.local:27017"},
          { _id : 1, host : "Jeffreys-MacBook-Pro.local:27018"},
          { _id : 2, host : "Jeffreys-MacBook-Pro.local:27019"} ]
};

rs.initiate(config);
rs.status();



