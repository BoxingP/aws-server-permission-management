# Server Permission Management

## Introduction

This GitHub repository is intended to manage SSH key access for users involved in a project. It
contains script that allow you to add or remove SSH public key on relevant servers, maintaining secure and controlled
access.

## Prerequisites

Before running the script, ensure that you have:

1. Initiate the process by preparing the necessary keys. Ensure that these keys are saved in the root path of the
   project directory and the names are set up in [.env](.env) file.
2. Update the values in [.env](.env) file, ensuring that the environment variables are updated accurately according to
   the actual ones.

## Usage

The repository comes with one main script: [modify_authorized_keys_file.py](modify_authorized_keys_file.py).

### Add SSH Public Key

To add the public key to the servers, execute the following command. This script appends the provided public key
to `SSH_USER_AUTHORIZED_KEYS_FILE` defined in [.env](.env).

```bash
python modify_authorized_keys_file.py add
```

### Delete SSH Public Key

To delete the public key from the servers, execute the following command. This script removes the mentioned public
from `SSH_USER_AUTHORIZED_KEYS_FILE` defined in [.env](.env).

```bash
python modify_authorized_keys_file.py remove
```

