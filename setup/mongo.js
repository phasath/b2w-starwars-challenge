var db = connect('127.0.0.1:27017/star_wars_planets');

db.createUser({
    user: "obi_wan",
    pwd: "kenobi",
    roles: [{
        role: "readWrite",
        db: "star_wars_planets"
    }, {
        role: "dbOwner",
        db: "star_wars_planets"
    }]
});

db.createCollection('planets', {autoIndexId: true});