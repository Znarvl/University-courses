#!/bin/sh

for A in dot neato fdp sfdp twopi circo; do
  for B in svg png ps; do
    for C in 1 2; do
      $A -T $B -o example$C.$A.$B example$C.dot
    done
  done
done
