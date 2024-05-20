#!/bin/bash
RUST_FILES_DIR="`dirname "$0"`/src"
RUST_FILES=`find $RUST_FILES_DIR -type f -name "*.rs"`
for rust_file in $RUST_FILES; do
    rustfmt $rust_file
done
