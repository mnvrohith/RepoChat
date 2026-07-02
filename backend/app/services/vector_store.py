from app.database.mongodb import collection


class VectorStore:
    """
    Store and retrieve code chunks.
    """

    def insert_chunk(self, chunk: dict):
        result = collection.insert_one(chunk)
        return str(result.inserted_id)

    def search(
        self,
        query_embedding,
        project_id: str,
        limit: int = 5,
    ):

        pipeline = [
            {
                "$vectorSearch": {
                    "index": "code_vector_index",
                    "path": "embedding",
                    "queryVector": query_embedding,
                    "numCandidates": 100,
                    "limit": limit,
                    "filter": {
                        "project_id": project_id
                    }
                }
            },
            {
                "$project": {
                    "_id": 0,
                    "project_id": 1,
                    "name": 1,
                    "file_path": 1,
                    "text": 1,
                    "score": {
                        "$meta": "vectorSearchScore"
                    },
                }
            },
        ]

        return list(collection.aggregate(pipeline))