# Trie Implementation in Python

This repository contains an implementation of a Trie (prefix tree) data structure in Python. The Trie is used to store sentences and retrieve them based on a query.

## Main Features

- **Insertion**: Sentences can be inserted into the Trie using the `_insert` method. Each word in the sentence is broken down into characters and inserted into the Trie.

- **Node Retrieval**: A specific node in the Trie can be retrieved based on a provided query using the `_get_target_node` method.

- **Querying**: The main logic of the code is in the first method. It traverses the Trie based on the provided query and retrieves all sentences that start with the query.

## Known Issues

Currently, the code cannot retrieve sentences with the same prefixes. This is a known issue and will be addressed in future updates.

## Usage

To use this code, simply import the Trie class and create an instance of it. You can then use the provided methods to interact with the Trie.

## Contributing

Contributions are welcome. Please submit a pull request with any improvements or bug fixes.

## License

This project is licensed under the MIT License.