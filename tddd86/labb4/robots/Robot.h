/**
 * Copyright (C) David Wolfe, 1999.  All rights reserved.
 * Ported to Qt and adapted for TDDD86, 2015.
 */

#ifndef ROBOT_H
#define ROBOT_H

#include "Unit.h"
#include <QGraphicsScene>

// For comments see Unit
class Robot : public Unit {
public:
    Robot();
    Robot(const Unit& c);

    /*
     * Creates a clone of the object
     */
    virtual Robot* clone();

    /*
     * Returns if the object is Junk as bool.
     */
    virtual bool isJunk() const;

    void draw(QGraphicsScene* scene) const override;
};

#endif // ROBOT_H
