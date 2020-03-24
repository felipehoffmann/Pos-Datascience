# Pos-Datascience
Exercicios de MongoDB

1.1 - db.pets.insert({name:"Frodo",species:"Peixe"})

1.1 - db.pets.insert({name:"Frodo",species:"Hamster"})

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

2.4 - db.italians.find({dog: {$exists: true}}).count()

      db.italians.find({cat: {$exists: true}}).count()
 
      db.italians.find({cat: {$exists: false}, dog: {$exists: false}}).count()

2.5 - db.italians.find({age: {'$gt': 60}, cat: {$exists: true}}).count()

2.6 - db.italians.find({age: {'$gte': 12, '$lte': 18}, dog: {$exists: true}}).count()

2.7 - db.italians.find({$where: "this.dog && this.cat"})

2.8 - db.italians.find({$where: "this.cat && this.age < this.cat.age"})

2.9 - db.italians.find({$where: "(this.dog && this.firstname == this.dog.name) || (this.cat && this.firstname == this.cat.name)"})

2.10 - db.italians.find({bloodType: /-/}, {firstname: true, surname: true})

2.11 - db.italians.find({}, {_id: false, cat: true, dog: true})

2.12 - db.italians.find({surname: 'Rossi'}).sort({age:-1}).limit(5)

2.13 - 
