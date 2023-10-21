#!/bin/bash


# Get the directory where the script is located
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# Function to install the app
package_app() {
  # Compile the tar file
  tar -cvf "$SCRIPT_DIR/smarteye-lite.tar backend/"
}

package_app