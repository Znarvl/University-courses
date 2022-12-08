package platform.game;

import platform.game.map.Background;
import platform.game.map.Viewer;
import platform.game.map.WindowComponent;
import platform.game.objects.Bullet;
import platform.game.objects.Enemy;
import platform.game.objects.Player;
import platform.game.objects.PowerUp;
import platform.game.states.State;

import java.util.ArrayList;
import java.util.List;
import java.util.Random;

public class GameEngine
{

    private Player player;
    private Background background;

    private List<Enemy> enemiesToRemove;
    private List<Enemy> stillLivingEnemies;

    private List<PowerUp> powerUpList;
    private boolean removePowerUp;

    private List<Bullet> bulletList;
    private List<Bullet> bulletsToRemove;

    public GameEngine(final Player player, Background background) {
	this.player = player;
	this.background = background;


	// Enemy things
	enemiesToRemove    = new ArrayList<>();
	stillLivingEnemies = new ArrayList<>();


	// Powerup things
	removePowerUp      = false;
	powerUpList	   = new ArrayList<>();

	// Bullet things
	bulletList 	   = new ArrayList<>();
	bulletsToRemove    = new ArrayList<>();

    }

    public Player getPlayer() {
	return player;
    }

    public Background getBackground() {
	return background;
    }

    public List<Bullet> getBulletList() {
	return bulletList;
    }

    public List<PowerUp> getPowerUpList() {
	return powerUpList;
    }

    public List<Enemy> getStillLivingEnemies() {
	return stillLivingEnemies;
    }

    private void spawnPowerUp(){
	int rnd = (int)Math.floor(Math.random() * 10);
	if (rnd == 5 && powerUpList.isEmpty() && !player.isPoweredUp()) {
	    powerUpList.add(new PowerUp(Viewer.getWIDTH() - PowerUp.WIDTH, Background.getBottom() - PowerUp.HEIGHT));
	    removePowerUp = false;
	}
    }


    // Bullet things

    public void shoot() {
        if (player.getShootTimer() == player.getShootDelay()) {
	    bulletList.add(new Bullet(player));
	    player.setShootTimer(0);
	}
    }

    public void gameTick(Player player){

	if(WindowComponent.getState() == State.GAME) {

	    player.playerTick();
	    spawnPowerUp();

	    bulletsToRemove.clear();
	    enemiesToRemove.clear();

	    for (Enemy enemy : stillLivingEnemies) {
	        enemy.enemyTick();
			if (enemy.getX() == 0 || player.hasCollision(enemy)) {
			    enemiesToRemove.add(enemy);
			    player.setHealth(player.getHealth() - 2);
			    System.out.println(player.getHealth());
			    if (player.getHealth() == 0) {
				System.exit(0);
			    }
			}
	    }


	    for (PowerUp powerup : powerUpList){
	   	        if (player.getLeft() >= powerup.getLeft() && player.getLeft() <= powerup.getRight() &&
			    player.getBottom() >= powerup.getTop() ||
			    player.getRight() <= powerup.getRight() && player.getRight() >= powerup.getLeft() &&
			    player.getBottom() >= powerup.getTop()) {

	   	            player.setPoweredUp(true);
	   	            player.setBeenPowerdUp(0);
	   	            removePowerUp = true;
	   		}
	   	        if (powerup.getX() <= 0){
	   	            removePowerUp = true;
	   		}
	   	    }

	   	    if(removePowerUp || player.isPoweredUp()){
	   	        powerUpList.clear();
	   	    }


	    for (Bullet bullet : bulletList) {
		bullet.bulletTick();
		if (bullet.outOfView()) {
		    bulletsToRemove.add(bullet);
		}

		for (Enemy enemy : stillLivingEnemies) {

		    if (bullet.hitEnemy(enemy)) {
		        enemiesToRemove.add(enemy);
		        bulletsToRemove.add(bullet);
		    }
		}
	    }

	    //Removes the enemies that should be removed
	    for (Enemy enemy : enemiesToRemove) {
		stillLivingEnemies.remove(enemy);
	    }

	    //Removes the bullets that should be removed
	    for (Bullet bullet : bulletsToRemove) {
		bulletList.remove(bullet);
	    }

	    //Spawn new enemies
	    spawnEnemy();

	}
    }



    private void spawnEnemy() {
 	int rnd = (int)Math.floor(Math.random() * 200) + 1;
 		if (rnd == 5) {
 		    Random ran = new Random();
 		    int i = ran.nextInt(Background.getBottom() - Player.getPLAYERHEIGHT()) + 1;
		    stillLivingEnemies.add(new Enemy(i));
 		}
    }

}
