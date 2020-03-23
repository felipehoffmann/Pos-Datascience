# Pos-Datascience
Exercicios de Neo4J

1.1 - MATCH(n) return n;

1.2 - CALL db.schema();

1.3 - MATCH(n:Person) return n;

1.4 - MATCH(n:Movie) return n;


2.1 - MATCH(n:Movie {released:2003}) return n;

2.2 - Exercise 2-2.png

2.3 - CALL db.propertyKeys;

2.4 - match(n:Movie {released:2006}) return n.title;

2.5 - match(n:Movie) return n.title, n.released, n.tagline;

2.6 - MATCH (m:Movie) RETURN m.title AS `Título do filme`, m.released AS `Ano de lançamento`, m.tagline AS `Slogan`;


3.1 - CALL db.schema();

3.2 - MATCH (p:Person)-[:WROTE]->(:Movie {title: 'Speed Racer'}) RETURN p.name;

3.3 - MATCH (m:Movie)<--(:Person {name: 'Tom Hanks'}) RETURN m.title;

3.4 - MATCH (m:Movie)-[rel]-(:Person {name: 'Tom Hanks'}) RETURN m.title, type(rel);

3.5 - MATCH (m:Movie)-[rel:ACTED_IN]-(p:Person {name: 'Tom Hanks'}) RETURN m.title, rel.roles;


4.1 - MATCH (p:Person)-[:ACTED_IN]->(m:Movie)

      WHERE p.name = 'Tom Cruise'
      
      RETURN m.title;
      
4.2 - MATCH (p:Person)

      WHERE p.born >= 1970
      
        and p.born < 1980
        
      RETURN p.name, p.born;
      
4.3 - MATCH (p:Person)-[:ACTED_IN]->(m:Movie)

      WHERE p.born > 1960
      
        and m.title = 'The Matrix'
        
      RETURN p.name, p.born;
      
4.4 - MATCH (m:Movie)

      WHERE m.released = 2000
      
      RETURN m.title;
      
4.5 - MATCH (p:Person)-[:WROTE]->(m:Movie) RETURN p.name, m.title;

4.6 - MATCH (p:Person)

      WHERE not exists(p.born)
      
      RETURN p.name;
      
4.7 - MATCH (p:Person)-[rel]-(m:Movie)

      WHERE exists(rel.rating)
      
      RETURN p.name as `Pessoa`, m.title as `Filme`, rel.rating as `Rating`;
      
4.8 - MATCH (p:Person)-[:ACTED_IN]->(m:Movie)

      WHERE p.name starts with 'James'
      
      RETURN distinct(p.name) as `Pessoa`;
      
4.9 - MATCH (p:Person)-[r:REVIEWED]->(m:Movie)

      WHERE tolower(r.summary) contains 'fun'
      
      RETURN m.title as `Filme`, r.summary as Review, r.rating as Rating;
      
4.10 - MATCH (p:Person)-[:PRODUCED]->(m:Movie)

       WHERE NOT ((p)-[:DIRECTED]->(:Movie))
       
       RETURN p.name, m.title;
       
4.11 - MATCH (p1:Person)-[:ACTED_IN]->(m:Movie)<-[:ACTED_IN]-(p2:Person)

       WHERE exists( (p2)-[:DIRECTED]->(m) )
       
       RETURN p1.name as Ator, p2.name as `Ator/Diretor`, m.title as Filme;
       
4.12 - MATCH(m:Movie)

       WHERE m.released in [2000, 2004, 2008]
       
       RETURN m.title, m.released;
       
4.13 - MATCH (p:Person)-[r:ACTED_IN]->(m:Movie)

       WHERE m.title in r.roles
       
       RETURN  m.title as Filme, p.name as Ator;
       

5.1 - MATCH (a:Person)-[:ACTED_IN]->(m:Movie)<-[:DIRECTED]-(d:Person),

            (a2:Person)-[:ACTED_IN]->(m)
            
      WHERE a.name = 'Gene Hackman'
      
      RETURN m.title as Filme, d.name AS Diretor , a2.name AS `Co-atores`;
      
5.2 - MATCH(p1:Person)<-[:FOLLOWS]->(p2:Person)

      WHERE p1.name = 'James Thompson'
      
      RETURN p1, p2;
      
5.3 - MATCH (p1:Person)-[:FOLLOWS*3]-(p2:Person)

      WHERE p1.name = 'James Thompson'
      
      RETURN p1, p2;
      
5.4 - MATCH (p1:Person)-[:FOLLOWS*1..2]-(p2:Person)

      WHERE p1.name = 'James Thompson'
      
      RETURN p1, p2;
      
5.5 - MATCH (p1:Person)-[:FOLLOWS*]-(p2:Person)

      WHERE p1.name = 'James Thompson'
      
      RETURN p1, p2;
      
5.6 - MATCH (p:Person)

      WHERE p.name STARTS WITH 'Tom'
      
      OPTIONAL MATCH (p)-[:DIRECTED]->(m:Movie)
      
      RETURN p.name, m.title;
      
5.7 - MATCH (p:Person)-[:ACTED_IN]->(m:Movie)

      RETURN p.name as actor, collect(m.title) AS `Filmes`;
      
5.8 - MATCH (p:Person)-[:ACTED_IN]->(m:Movie)<-[:ACTED_IN]-(p2:Person)

      WHERE p.name = 'Tom Cruise'
      
      RETURN m.title as Filme, collect(p2.name) AS `Co-atores`;
      
5.9 - MATCH (p:Person)-[:REVIEWED]->(m:Movie)

      RETURN m.title as Filme, count(p) as numReviews, collect(p.name) as Reviewers;
      
5.10 - MATCH (d:Person)-[:DIRECTED]->(m:Movie)<-[:ACTED_IN]-(a:Person)

       RETURN d.name AS Diretor, count(a) AS `Número de atores` , collect(a.name) AS `Actores com quem trabalhou`;
       
5.11 - MATCH (a:Person)-[:ACTED_IN]->(m:Movie)

       WITH  a, count(a) AS numFilmes, collect(m.title) AS filmes
       
       WHERE numFilmes = 5
       
       RETURN a.name, filmes;
       
5.12 - MATCH (m:Movie)

       WITH m, size((:Person)-[:DIRECTED]->(m)) AS directors
       
       WHERE directors >= 2
       
       OPTIONAL MATCH (p:Person)-[:REVIEWED]->(m)
       
       RETURN  m.title, p.name;
       

6.1 - MATCH (a:Person)-[:ACTED_IN]->(m:Movie)

      WHERE m.released >= 1990 AND m.released < 2000
      
      RETURN DISTINCT m.released, m.title, collect(a.name);
      
6.2 - MATCH (a:Person)-[:ACTED_IN]->(m:Movie)

      WHERE m.released >= 1990 AND m.released < 2000
      
      RETURN  m.released, collect(m.title), collect(a.name);
      
6.3 - MATCH (a:Person)-[:ACTED_IN]->(m:Movie)

      WHERE m.released >= 1990 AND m.released < 2000
      
      RETURN  m.released, collect(DISTINCT m.title), collect(a.name);
      
6.4 - MATCH (a:Person)-[:ACTED_IN]->(m:Movie)

      WHERE m.released >= 1990 AND m.released < 2000
      
      RETURN  m.released, collect(DISTINCT m.title), collect(a.name)
      
      ORDER BY m.released DESC;
      
6.5 - MATCH (:Person)-[r:REVIEWED]->(m:Movie)

      RETURN  m.title AS movie, r.rating AS rating
      
      ORDER BY r.rating DESC LIMIT 5;
      
6.6 - MATCH (a:Person)-[:ACTED_IN]->(m:Movie)

      WITH  a,  count(a) AS numMovies, collect(m.title) AS movies
      
      WHERE numMovies <= 3
      
      RETURN a.name, movies;      
      

7.1 - MATCH (a:Person)-[:ACTED_IN]->(m:Movie), (m)<-[:PRODUCED]-(p:Person)

      WITH  m, collect(DISTINCT a.name) AS cast, collect(DISTINCT p.name) AS producers
      
      RETURN DISTINCT m.title, cast, producers
      
      ORDER BY size(cast);
      
7.2 - MATCH (p:Person)-[:ACTED_IN]->(m:Movie)

      WITH p, collect(m) AS movies
      
      WHERE size(movies)  > 5
      
      RETURN p.name, movies;
      
7.3 - MATCH (p:Person)-[:ACTED_IN]->(m:Movie)

      WITH p, collect(m) AS movies
      
      WHERE size(movies)  > 5
      
      WITH p, movies UNWIND movies AS movie
      
      RETURN p.name, movie.title;
      
7.4 - MATCH (a:Person)-[:ACTED_IN]->(m:Movie)

      WHERE a.name = 'Tom Hanks'
      
      RETURN  m.title, m.released, date().year  - m.released as yearsAgoReleased, m.released  - a.born AS `age of Tom`
      
      ORDER BY yearsAgoReleased;
      

8.1 - CREATE (:Movie {title: 'Forrest Gump'});

8.2 - MATCH (m:Movie)

      WHERE m.title = 'Forrest Gump'
      
      RETURN m;
      
8.3 - CREATE (:Person {name: 'Robin Wright'});

8.4 - MATCH (p:Person)

      WHERE p.name = 'Robin Wright'
      
      RETURN p;
      
8.5 - MATCH (m:Movie)

      WHERE m.released < 2010
      
      SET m:OlderMovie
      
      RETURN DISTINCT labels(m);
      
8.6 - MATCH (m:OlderMovie) RETURN m.title, m.released;

8.7 - MATCH (p:Person)

      WHERE p.name STARTS WITH 'Robin'
      
      SET p:Female;
      
8.8 - MATCH (p:Female) RETURN p.name;

8.9 - MATCH (p:Female) REMOVE p:Female;

8.10 - CALL db.schema;

8.11 - MATCH (m:Movie)

       WHERE m.title = 'Forrest Gump'
       
       SET m:OlderMovie,
       
           m.released = 1994,
           
           m.tagline = "Life is like a box of chocolates...you never know what you're gonna get.",
           
           m.lengthInMinutes = 142;
           
8.12 - MATCH (m:OlderMovie)

       WHERE m.title = 'Forrest Gump'
       
       RETURN m;
       
8.13 - MATCH (p:Person)

       WHERE p.name = 'Robin Wright'
       
       SET p.born = 1966, p.birthPlace = 'Dallas';
       
8.14 - MATCH (p:Person)

       WHERE p.name = 'Robin Wright'
       
       RETURN p;
       
8.15 - MATCH (m:Movie)

       WHERE m.title = 'Forrest Gump'
       
       SET m.lengthInMinutes = null;
       
8.16 - MATCH (m:Movie)

       WHERE m.title = 'Forrest Gump'
       
       RETURN m;
       
8.17 - MATCH (p:Person)

       WHERE p.name = 'Robin Wright'
       
       REMOVE p.birthPlace;
       
8.18 - MATCH (p:Person)

       WHERE p.name = 'Robin Wright'
       
       RETURN p;
       


9.1 - MATCH (m:Movie)

      WHERE m.title = 'Forrest Gump'
      
      MATCH (p:Person)
      
      WHERE p.name = 'Tom Hanks' OR p.name = 'Robin Wright' OR p.name = 'Gary Sinise'
      
      CREATE (p)-[:ACTED_IN]->(m);
      
9.2 - MATCH (m:Movie)

      WHERE m.title = 'Forrest Gump'
      
      MATCH (p:Person)
      
      WHERE p.name = 'Robert Zemeckis'
      
      CREATE (p)-[:DIRECTED]->(m);
      
9.3 - MATCH (p1:Person)

      WHERE p1.name = 'Tom Hanks'
      
      MATCH (p2:Person)
      
      WHERE p2.name = 'Gary Sinise'
      
      CREATE (p1)-[:HELPED]->(p2);
      
9.4 - MATCH (p:Person)-[rel]-(m:Movie)

      WHERE m.title = 'Forrest Gump'
      
      RETURN p, rel, m;
      
9.5 - MATCH (p:Person)-[rel:ACTED_IN]->(m:Movie)

      WHERE m.title = 'Forrest Gump'
      
      SET rel.roles =
      
      CASE p.name
      
        WHEN 'Tom Hanks' THEN ['Forrest Gump']
        
        WHEN 'Robin Wright' THEN ['Jenny Curran']
        
        WHEN 'Gary Sinise' THEN ['Lieutenant Dan Taylor']
        
      END;
      
9.6 - MATCH (p1:Person)-[rel:HELPED]->(p2:Person)

      WHERE p1.name = 'Tom Hanks' AND p2.name = 'Gary Sinise'
      
      SET rel.research = 'war history';
      
9.7 - call db.propertyKeys;

9.8 - call db.schema;

9.9 - MATCH (p:Person)-[rel:ACTED_IN]->(m:Movie)

      WHERE m.title = 'Forrest Gump'
      
      RETURN p.name, rel.roles;
      
9.10 - MATCH (p1:Person)-[rel:HELPED]-(p2:Person) RETURN p1.name, rel, p2.name;

9.11 - MATCH (p:Person)-[rel:ACTED_IN]->(m:Movie)

       WHERE m.title = 'Forrest Gump' AND p.name = 'Gary Sinise'
       
       SET rel.roles =['Lt. Dan Taylor'];
       
9.12 - MATCH (p1:Person)-[rel:HELPED]->(p2:Person)

       WHERE p1.name = 'Tom Hanks' AND p2.name = 'Gary Sinise'
       
       REMOVE rel.research;
       
9.13 - MATCH (p:Person)-[rel:ACTED_IN]->(m:Movie)

       WHERE m.title = 'Forrest Gump'
       
       return p, rel, m;
       

10.1 - MATCH (:Person)-[rel:HELPED]-(:Person) DELETE rel;

10.2 - MATCH (:Person)-[rel:HELPED]-(:Person) RETURN rel;

10.3 - MATCH (p:Person)-[rel]-(m:Movie)

       WHERE m.title = 'Forrest Gump'
       
       RETURN p, rel, m;
       
10.4 - MATCH (m:Movie)

       WHERE m.title = 'Forrest Gump'
       
       DELETE m;
       
10.5 - MATCH (m:Movie)

       WHERE m.title = 'Forrest Gump'
       
       DETACH DELETE m;
       
10.6 - MATCH (p:Person)-[rel]-(m:Movie)

       WHERE m.title = 'Forrest Gump'
       
       RETURN p, rel, m;
