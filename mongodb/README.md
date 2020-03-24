# Pos-Datascience
Exercicios de MongoDB

1.1.1 - db.pets.insert({name:"Frodo",species:"Peixe"})

1.1.2 - db.pets.insert({name:"Frodo",species:"Hamster"})

1.2 - db.pets.find({}).count()

1.3 - db.pets.findOne({})

1.4 - db.pets.find({name:'Kilha', species:'Gato'}, {_id: 1})

1.5 - db.pets.find({"_id" : ObjectId("5e794360209aaeb8db096514")})

1.6 - db.pets.find({species:'Hamster'})

1.7 - db.pets.find({name:'Mike'})

1.8 - db.pets.find({name:'Mike', species: 'Cachorro'})


2.1 - db.italians.find({age:99}).count()

2.2 - db.italians.find({age: {"$gt":65}}).count()

2.3 - db.italians.find({age: {"$gte":12, "$lte":18}})

2.4.1 - db.italians.find({dog: {$exists: true}}).count()

2.4.2 - db.italians.find({cat: {$exists: true}}).count()
 
2.4.3 - db.italians.find({cat: {$exists: false}, dog: {$exists: false}}).count()

2.5 - db.italians.find({age: {'$gt': 60}, cat: {$exists: true}}).count()

2.6 - db.italians.find({age: {'$gte': 12, '$lte': 18}, dog: {$exists: true}}).count()

2.7 - db.italians.find({$where: "this.dog && this.cat"})

2.8 - db.italians.find({$where: "this.cat && this.age < this.cat.age"})

2.9 - db.italians.find({$where: "(this.dog && this.firstname == this.dog.name) || (this.cat && this.firstname == this.cat.name)"})

2.10 - db.italians.find({bloodType: /-/}, {firstname: true, surname: true})

2.11 - db.italians.find({}, {_id: false, cat: true, dog: true})

2.12 - db.italians.find({surname: 'Rossi'}).sort({age:-1}).limit(5)

2.13 - db.italians.insert({firstname: "Antonio", lion: {name: "Simba", age: 8}})

2.14 - db.italians.remove({_id: ObjectId("5e7a5366b9ae8f804196449e")})

2.15.1 - db.italians.update({}, {"$inc": {"age":1}}, {multi: true})

2.15.2 - db.italians.update({$where: "this.cat"}, {"$inc": {"cat.age":1}}, {multi: true})

2.15.3 - db.italians.update({$where: "this.dog"}, {"$inc": {"dog.age":1}}, {multi: true})

2.16 - db.italians.remove({age: 66, $where: "this.cat"})

2.17 - db.italians.aggregate([{$match: { mother: {$exists: 1} }}, {$project: { firstname: 1, mother: 1, isEqual: { $cmp: ["$firstname", "$mother.firstname"]} }}, {$match: {"isEqual": 0}}])

2.18 - db.italians.aggregate({$group: {_id: "$firstname"}})

2.19 - db.italians.aggregate({$group: {_id: {name:"$firstname", surname: "$surname"}}})

2.20 - db.italians.find({age: {$gt: 20, $lt: 60}, favFruits: {$all: ["Banana", "Maçã"]}, $where: "this.cat" || "this.dog"})


3 - Stockbrokers

3.1 - db.stocks.find({"Profit Margin": {$gt: 0.5}}).limit(10)

3.2 - db.stocks.find({"Profit Margin": {$lt: 0}}).limit(10)

3.3 - db.stocks.find({}).sort({"Profit Margin":-1}).limit(10)

3.4 - db.stocks.aggregate([{$group: {_id: "$Sector", profit: {$avg: "$Profit Margin"}}}, {$sort: {profit: -1}}, {$limit: 1}])

3.5.1 - var myCursor = db.stocks.find({}).sort({"Profit Margin": -1});

3.5.2 - while (myCursor.hasNext()) { print(tojson(myCursor.next())); }

3.6 - db.stocks.update({}, {$rename: {"Profit Margin": "profit"}}, {multi: true});

3.7 - db.stocks.aggregate([{$group: {_id: "$Company", profit: {$avg: "$profit"}}}])

3.8.1 - db.stocks.find({}).sort({"EPS growth next 5 years": -1}).limit(3)

3.8.2 - Investiria nas 3 ações com maior previsão de retorno nos próximos 5 anos.

3.9 - db.stocks.find({}).sort({"Sector": 1})


3 - Enron

3.1 - db.stocks.aggregate({$group: {_id: "$sender"}})

3.2 - db.stocks.find({"$or": [{text: /fraud/}, {subject: /fraud/}]}).count()
