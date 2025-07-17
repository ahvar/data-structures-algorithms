import requests
import json
import hashlib
from hashlib import blake2b

class TraitHasher:
    def __init__(self, url):
        self._url = url
        self._json = {}
        self._hashed_traits = []

    def get_json(self):
        """
        Send a GET request to the URL and pull down the JSON data
        """
        response = requests.get(self._url)
        if response.status_code == 200:
            try:
                self._json = response.json()
                print(f"Retrieved data: {self._json}")
            except requests.exceptions.JSONDecodeError:
                print("Problem converting response to json")
                raise
        else:
            print(f"Request failed: {response.status_code}")
            raise requests.exceptions.RequestException(f"HTTP {response.status_code}")
    
    def hash_the_traits(self):
        """
        Hash the traits in the trait array and store them in the
        hashed traits array
        """
        self._hashed_traits = []  # Clear any existing hashes
        
        try:
            if "traits" not in self._json or "key" not in self._json:
                raise KeyError("Missing 'traits' or 'key' in response")
                
            for trait in self._json["traits"]:
                hobj = hashlib.blake2b(trait.encode('utf-8'), 
                                     digest_size=64, 
                                     key=self._json['key'].encode('utf-8'))
                digest = hobj.hexdigest()
                print(f"{trait} -> {digest}")
                self._hashed_traits.append(digest)
        except KeyError as ke:
            print(f"Required data not found: {ke}")
            raise
        except Exception as e:
            print(f"Something unexpected occurred: {e}")
            raise

    def post_hashed_traits(self):
        """
        Post the hashed traits array back to the URL
        """
        try:
            if not self._hashed_traits:
                raise ValueError("No hashed traits to post")
                
            print(f"Posting {len(self._hashed_traits)} hashes")
            print(f"First hash: {self._hashed_traits[0]}")
            print(f"Hash length: {len(self._hashed_traits[0])}")
            
            post_response = requests.post(self._url, json=self._hashed_traits)
            if post_response.status_code == 200:
                print("POST successful")
                print(post_response.text)
            else:
                print(f"POST failed: {post_response.status_code}")
                print(f"Error: {post_response.text}")
                raise requests.exceptions.RequestException(f"POST failed with status {post_response.status_code}")
        except requests.exceptions.RequestException:
            print("Request exception occurred during POST")
            raise
        except Exception as e:
            print(f"Unexpected error during POST: {e}")
            raise

    @property
    def hashed_traits(self):
        return self._hashed_traits

if __name__ == "__main__":
    buildwithus = "https://api.close.com/buildwithus/"
    trait_hasher = TraitHasher(buildwithus)
    trait_hasher.get_json()
    trait_hasher.hash_the_traits()
    trait_hasher.post_hashed_traits()




