import random
import typing


def gen_event() -> typing.Generator[tuple, None, None]:
    players = ["alice", "bob", "charlie", "dylan"]
    actions = [
        "run",
        "eat",
        "sleep",
        "grab",
        "move",
        "climb",
        "swim",
        "release",
        "use",
    ]

    while True:
        player = random.choice(players)
        action = random.choice(actions)
        yield (player, action)


def consume_event(event_list) -> typing.Generator[tuple, None, None]:
    while len(event_list) > 0:
        index = random.randint(0, len(event_list) - 1)
        chosen_event = event_list[index]
        event_list[:] = event_list[:index] + event_list[index + 1:]
        yield chosen_event


def ft_data_stream():
    print("=== Game Data Stream Processor ===")

    event_stream = gen_event()

    for i in range(1000):
        event = next(event_stream)
        print(f"Event {i}: Player {event[0]} did action {event[1]}")

    ten_events_list = [next(event_stream) for _ in range(10)]

    print(f"Built list of 10 events: {ten_events_list}")

    for event in consume_event(ten_events_list):
        print(f"Got event from list: {event}")
        print(f"Remains in list: {ten_events_list}")


if __name__ == "__main__":
    ft_data_stream()
