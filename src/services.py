import os
from dataclasses import dataclass
from supabase import Client, create_client


@dataclass
class FileService:
    client: Client = create_client(
        supabase_url=os.getenv('SUPABASE_URL'),
        supabase_key=os.getenv('SUPABASE_KEY')
    )

    def upload_file(self, bucket: str, path: str, file: bytes):
        self.client.storage.from_(bucket).upload(path, file)
        return self.client.storage.from_(bucket).get_public_url(path)
    
    def remove_file(self, bucket: str, *paths: str):
        self.client.storage.from_(bucket).remove(*paths)