from app.database.mongodb import collection


class VectorStore:
    """
    Store and retrieve code chunks.
    """

    def insert_chunk(self, chunk: dict):
        result = collection.insert_one(chunk)
        return str(result.inserted_id)

    def search(self, query_embedding, limit=5):

        pipeline = [
            {
                "$vectorSearch": {
                    "index": "code_vector_index",
                    "path": "embedding",
                    "queryVector": query_embedding,
                    "numCandidates": 100,
                    "limit": limit,
                }
            },
            {
                "$project": {
                    "_id": 0,
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