import pynecone as pc

class PyneconeprojectConfig(pc.Config):
    pass

config = PyneconeprojectConfig(
    app_name="pynecone_project",
    db_url="sqlite:///pynecone.db",
    env=pc.Env.DEV,
)
