var db = connect('127.0.0.1:27017/star_wars_planets_test');

db.createUser({
    user: "chewbacca",
    pwd: "GGGWARRRHHWWWW",
    roles: [{
        role: "readWrite",
        db: "star_wars_planets_test"
    }, {
        role: "dbOwner",
        db: "star_wars_planets_test"
    }]
});

db.createCollection('planets', {autoIndexId: true});