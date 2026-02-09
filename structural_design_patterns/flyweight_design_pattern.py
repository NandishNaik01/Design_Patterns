"""
FLYWEIGHT PATTERN – DATABASE MAPPING (EXECUTABLE DEMO)

Key idea:
- Shared data is stored once (Flyweight)
- Users reference shared data via an ID
- This mimics DB normalization using foreign keys
"""

from dataclasses import dataclass


# ------------------------------
# FLYWEIGHT (Intrinsic State)
# ------------------------------
@dataclass(frozen=True)
class UserMetadata:
    department: str
    role: str
    location: str


# ------------------------------
# FLYWEIGHT FACTORY
# (Simulates DB table + UNIQUE constraint)
# ------------------------------
class UserMetadataTable:
    """
    This class simulates a database table:

    TABLE user_metadata
    -----------------------------------------
    id | department | role | location
    -----------------------------------------

    UNIQUE(department, role, location)
    """

    _table: dict[int, UserMetadata] = {}
    _index: dict[tuple, int] = {}
    _id_counter: int = 1

    @classmethod
    def get_or_create(cls, department: str, role: str, location: str) -> int:
        """
        PSEUDOCODE (DB LOGIC):

        BEGIN TRANSACTION

        SELECT id FROM user_metadata
        WHERE department = ?
          AND role = ?
          AND location = ?

        IF exists:
            return id
        ELSE:
            INSERT INTO user_metadata (...)
            return new id

        COMMIT
        """

        key = (department, role, location)

        # SELECT
        if key in cls._index:
            return cls._index[key]

        # INSERT
        metadata_id = cls._id_counter
        cls._id_counter += 1

        cls._table[metadata_id] = UserMetadata(*key)
        cls._index[key] = metadata_id

        return metadata_id

    @classmethod
    def count(cls) -> int:
        return len(cls._table)


# ------------------------------
# CONTEXT (Extrinsic State)
# ------------------------------
@dataclass
class User:
    id: int
    name: str
    metadata_id: int


# ------------------------------
# USER TABLE (Simulated DB)
# ------------------------------
class UserTable:
    """
    TABLE users
    -------------------------------
    id | name | metadata_id (FK)
    -------------------------------
    """

    _table: dict[int, User] = {}
    _id_counter: int = 1

    @classmethod
    def create_user(cls, name: str, department: str, role: str, location: str):
        # Get shared flyweight row
        metadata_id = UserMetadataTable.get_or_create(
            department, role, location
        )

        user = User(
            id=cls._id_counter,
            name=name,
            metadata_id=metadata_id
        )

        cls._table[cls._id_counter] = user
        cls._id_counter += 1

    @classmethod
    def count(cls) -> int:
        return len(cls._table)


# ------------------------------
# CLIENT
# ------------------------------
def main():
    """
    We will create MANY users,
    but only a FEW shared metadata rows.
    """

    users_to_create = [
        ("Alice", "Engineering", "Developer", "Bangalore"),
        ("Bob", "Engineering", "Developer", "Bangalore"),
        ("Charlie", "Engineering", "Developer", "Bangalore"),
        ("Diana", "HR", "Manager", "London"),
        ("Eve", "HR", "Manager", "London"),
    ]

    for user in users_to_create:
        UserTable.create_user(*user)

    print("Total users created:", UserTable.count())
    print("Unique metadata rows:", UserMetadataTable.count())

    print("\n--- Metadata Table ---")
    for mid, meta in UserMetadataTable._table.items():
        print(mid, meta)

    print("\n--- Users Table ---")
    for uid, user in UserTable._table.items():
        print(uid, user)


if __name__ == "__main__":
    main()
