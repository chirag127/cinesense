def droplet_cluster():
    # Create a cluster with a name
    with Cluster("main"):
        # Create a droplet with a name
        droplet1 = Droplet("html")
        droplet2 = Droplet("css")
    return [droplet1, droplet2]


def db_cluster():
    # Create a database with a name
    db = DbaasPrimary("My database")
    return db


def logstash_cluster():
    # Create a logstash with a name
    logstash = Logstash("Logstash service")
    return logstash


def create_diagram():
    # Create a diagram with a name, a filename, and a direction
    with Diagram(
        "data flow diagram", show=False, filename="my-diagram", direction="LR"
    ):
        droplet1, droplet2 = droplet_cluster()
        db = db_cluster()
        logstash = logstash_cluster()

        # Connect droplet1 and droplet2 to the database
        [droplet1, droplet2] >> db >> [droplet1, droplet2]
        # Connect droplet1, droplet2, and db to logstash
        [droplet1, droplet2, db] >> Edge(color="firebrick", style="dashed") >> logstash
        # Connect logstash to the database
        logstash >> Edge(color="green", style="dashed") >> db
