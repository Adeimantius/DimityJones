import hashlib

def load_text(filename):
    with open(filename, "r") as f:
        return f.read()
    
def compare_sha256_hashes(data, expected_hash):
  """
  Generates a SHA256 hash of the input data and compares it to the expected hash.

  Args:
    data: The data to hash (string or bytes-like object).
    expected_hash: The expected SHA256 hash (hexadecimal string).

  Returns:
    True if the generated hash matches the expected hash, False otherwise.
  """
  if isinstance(data, str):
    data = data.encode('utf-8') # Encode string to bytes
  
  hashed_data = hashlib.sha256(data).hexdigest()
  return hashed_data == expected_hash
