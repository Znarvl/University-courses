package org.simja649.multi;


import org.joda.time.LocalTime;
import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;

public class TimeRetriever {
    public static String getTimeMessage() {
        Logger logger = LogManager.getLogger(HelloMaven.class);
        LocalTime localTime = new LocalTime();

        logger.info("Requested time string: " + localTime.toString());
        return "TODO list: " + localTime.toString();
    }
}