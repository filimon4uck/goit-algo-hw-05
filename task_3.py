import timeit
from search_algorithms.boyer_moore_algorithm import boyer_moore_search
from search_algorithms.kmp_algorithm import kmp_search
from search_algorithms.rabin_karp_algorithm import rabin_karp_search


def load_file(filename):
    with open(filename, "r", encoding="utf-8") as file:
        return file.read()


def measure_time(func, text, pattern):
    return timeit.timeit(lambda: func(text, pattern), number=1)


def find_faster_algo(algorythms):
    for result in algorythms:
        print(f"{algorythms[result]} : {result}")
        return algorythms.get(min(algorythms.keys()))


def main():
    text1 = load_file("data/art1.txt")
    text2 = load_file("data/art2.txt")

    test_cases = [
        ("Existing substring in file1", text1, "Інтерполяційний пошук"),
        ("Existing substring in file2", text2, "Розгорнутий зв’язний"),
        ("Non-existing substring", text1, "Неіснуючий підрядок"),
    ]

    search_algo = [
        ("KMP", kmp_search),
        ("Boyer-Moore", boyer_moore_search),
        ("Rabin-Karp", rabin_karp_search),
    ]
    for description, text, substring in test_cases: 
        print(f"\n{description}:")
        results = {
            measure_time(algo[1], text, substring): algo[0] for algo in search_algo
        }
        for time_taken, algo_name in sorted(results.items()):
            print(f"{algo_name}: {time_taken:.6f} seconds")
        fastest = min(results.items())[1]
        print(f"Fastest: {fastest}")


if __name__ == "__main__":
    main()
