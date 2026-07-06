VALIDATE_LEETCODE_USER = """
query userPublicProfile($username: String!) {
  matchedUser(username: $username) {
    username
  }
}
"""