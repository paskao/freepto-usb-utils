#!/bin/bash


TMPDIR=$(mktemp -d)

echo $TMPDIR


LANGS=$(ls locale)

for LANG in $LANGS
do
    ORIGINAL_FILE="locale/$LANG/LC_MESSAGES/freepto-usb-utils.po"
    BASEPO="$TMPDIR/freepto-usb-utils.po"
    NEW_FILE="$TMPDIR/new.po"
    touch $BASEPO
    xgettext -L Python -o $BASEPO --package-name freepto-usb-utils --no-location --omit-header `pwd`/freepto-live-tray
    msgmerge -N $ORIGINAL_FILE $BASEPO > $NEW_FILE
    mv $NEW_FILE $ORIGINAL_FILE
    rm $BASEPO
done

rmdir $TMPDIR
