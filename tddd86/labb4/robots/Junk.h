/**
 * Copyright (C) David Wolfe, 1999.  All rights reserved.
 * Ported to Qt and adapted for TDDD86, 2015.
 *
 * Junk inherits properties from Robot
 */

#ifndef JUNK_H
#define JUNK_H

#include "Unit.h"
#include "Robot.h"
#include <QGraphicsScene>

// For comments see Robot
class Junk : public Robot {
public:
    Junk();
    Junk(const Robot& c);

    /*
    * Draws this junk onto the given QGraphicsScene.
    */
    void draw(QGraphicsScene* scene) const override;

    void moveTowards(const Unit& u) override;

    bool attacks(const Unit& u) const override;

    bool isJunk() const override;

    Junk* clone() override;
};

#endif // JUNK_H
