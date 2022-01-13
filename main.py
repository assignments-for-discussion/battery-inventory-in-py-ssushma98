
def count_batteries_by_usage(cycles):
  hashmap = { "lowCount": 0, "mediumCount": 0, "highCount": 0}
    for c in cycles:
        if c < 400:
            hashmap["lowCount"]+=1
        elif 400 <= c <= 919:
            hashmap["mediumCount"]+=1
        elif c >= 920:
            hashmap["highCount"]+=1
    return hashmap
  return {
    "lowCount": 0,
    "mediumCount": 0,
    "highCount": 0
  }


def test_bucketing_by_number_of_cycles():
  print("Counting batteries by usage cycles...\n");
  counts = count_batteries_by_usage([100, 300, 500, 600, 900, 1000])
  assert(counts["lowCount"] == 2)
  assert(counts["mediumCount"] == 3)
  assert(counts["highCount"] == 1)
  print("Done counting :)")


if __name__ == '__main__':
  test_bucketing_by_number_of_cycles()
