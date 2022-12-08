/**
 * Copyright (C) David Wolfe, 1999.  All rights reserved.
 * Ported to Qt and adapted for TDDD86, 2015.
 */

#include "GameState.h"
#include "utilities.h"
#include "constants.h"
#include <algorithm>


GameState::GameState(){}

GameState::GameState(int numberOfRobots) {
    for (int i = 0; i < numberOfRobots; i++) {
        Robot* robot;
        do {robot = new Robot();}
        while (!isEmpty (*robot));
        robots.push_back(robot);
    }
    teleportHero();
}

GameState::GameState(const GameState& state) {
    robots.reserve(state.robots.size());
    hero = state.hero;
    for (unsigned i = 0; i < state.robots.size(); i++) {
        robots.push_back(state.robots[i]->clone());
    }
   }

GameState::~GameState() {

    for (unsigned i = 0; i < robots.size(); i++) {
        delete robots[i];
    }
}

GameState& GameState::operator=(const GameState& state) {
    if(this !=&state)
    {// /*(this->robots.size() != state.robots.size()) || (this->heroDead() != state.heroDead())*/) {
        GameState newState(state);
        std::swap(robots, newState.robots);
        std::swap(hero, newState.hero);
    }
    return *this;
}

void GameState::draw(QGraphicsScene *scene) const {
    scene->clear();
    for (size_t i = 0; i < robots.size(); ++i)
        robots[i]->draw(scene);
    hero.draw(scene);
}

void GameState::teleportHero() {
    do hero.teleport();
    while (!isEmpty(hero));
}

void GameState::moveRobots() {
    for (unsigned int i = 0; i < robots.size(); i++)
        robots[i]->moveTowards (hero);
}

int GameState::countCollisions() {
    int numberDestroyed = 0;
    for(unsigned i = 0; i < robots.size(); i++) {
        bool collision = (countRobotsAt (*robots[i]) > 1);
        if (!robots[i]->isJunk() && collision) {
            Junk* junkyard = new Junk(*robots[i]);
            delete robots[i];
            robots[i] = junkyard;
            numberDestroyed++;
        }
    }
    return numberDestroyed;
}

bool GameState::anyRobotsLeft() const {
    for (unsigned i = 0 ; i < robots.size(); i++) {
        if(!robots[i]->isJunk()){
            return true;
        }
    }
    return false;
}

bool GameState::heroDead() const {
    return !isEmpty(hero);
}

bool GameState::isSafe(const Unit& unit) const {
    for (unsigned int i = 0; i < robots.size(); i++)
    {
        if (robots[i]->attacks(unit) ||(robots[i]->at(unit) && robots[i]->isJunk()) ) return false;

    }

    return true;
}

void GameState::moveHeroTowards(const Unit& dir) {
    hero.moveTowards(dir);
}

Hero GameState::getHero() const {return hero;}

/*
 * Free of robots and junk only
 */
bool GameState::isEmpty(const Unit& unit) const {
    return (countRobotsAt(unit) == 0);
}

/*
 * How many robots are there at unit?
 */
int GameState::countRobotsAt(const Unit& unit) const {
    int count = 0;
    for (size_t i = 0; i < robots.size(); ++i) {
        if (robots[i]->at(unit))
            count++;
    }
    return count;
}
