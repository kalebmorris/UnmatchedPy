import random
import sqlite3
from typing import List

HEROES: List[str] = [
    'Achilles',
    'Alice',
    'Bigfoot',
    'Bloody Mary',
    'King Arthur',
    'Medusa',
    'Robin Hood',
    'Sinbad',
    'Sun Wukong',
    'Yennenga',
]

ARENAS: List[str] = [
    'Marmoreal',
    'Hanging Gardens',
    'Sarpedon',
    'Sherwood Forest',
    'Yukon'
]

# Function to generate a fight
# Takes in an optional argument 'banned_heroes' which is a list of heroes not to include in the fight
# Returns a tuple of two heroes and the arena they are fighting in
def generate_fight(banned_heroes: List[str] = None) -> None:
    heroes = HEROES
    if banned_heroes:
        heroes = [hero for hero in heroes if hero not in banned_heroes]
    
    fighters = random.sample(heroes, 2)
    arena = random.choice(ARENAS)
    return (fighters[0], fighters[1], arena)

# Function to record the outcome of a fight
# Takes in the winning hero, losing hero, and arena as arguments
# Writes the fight result to a SQLite database
def record_fight(winningHero: str, losingHero: str, arena: str) -> None:
    if winningHero not in HEROES:
        raise ValueError(winningHero + " isn't an Unmatched hero.")
    if losingHero not in HEROES:
        raise ValueError(losingHero + " isn't an Unmatched hero.")
    if arena not in ARENAS:
        raise ValueError(arena + " is not an Unmatched arena.")

    conn = sqlite3.connect('/Users/kalebm/Python/unmatched/fights.db')
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS fights (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            winner TEXT,
            loser TEXT,
            arena TEXT
        )
    """)
    c.execute("""
        INSERT INTO fights (winner, loser, arena)
        VALUES (?, ?, ?)
    """, (winningHero, losingHero, arena))
    conn.commit()
    conn.close()

# Function to show the last <count> fights recorded in the database
def show_fights(count: int = 20) -> None:
    conn = sqlite3.connect('/Users/kalebm/Python/unmatched/fights.db')
    c = conn.cursor()
    c.execute(f"SELECT * FROM fights ORDER BY id DESC LIMIT {count}")
    fights = c.fetchall()
    print("{:<20} {:<20} {:<20}".format("Winner", "Loser", "Arena"))
    print(63 * "‾")
    for fight in fights:
        print("{:<20} {:<20} {:<20}".format(fight[1], fight[2], fight[3]))
    conn.close()
