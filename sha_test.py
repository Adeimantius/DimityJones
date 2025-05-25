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
  print(hashed_data)
  print(expected_hash)
  return hashed_data == expected_hash

#test_buffer = "To begin with, for example, and to make sure your SHA-256 hash function is working, the hash value or checksum of this sentence, from capital 'T' to concluding colon, expressed in hexadecimal, is:"
#input_text = test_buffer
#target_sha = "10c0c7d9b0222a5a61601337105f1cbb7b1723b991404b870537095d1174f2b2"
filepath = r"D:\dev\puzzles\DimityJones\solution-3.txt"
target_sha = "2f2c81c6f85a957ec494899f0e1ca52a3d4957aa5f71ed115db48657e62742bc"
input_text = load_text(filepath)

match = compare_sha256_hashes(input_text, target_sha)
print(match)