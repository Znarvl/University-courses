/*
This is an example of what cp --reflink=always does. It only works on
filesystems that support cloning of files. In most Linux filesystems,
you can hardlink two files, making them the same. But if you update
either file, both are updated (they are the same). With a reflink, when
you update one of the files a copy is created at that time (making the
write expensive but the copy fast); perhaps only creating copies of some
blocks in the file.

This is not part of the labs since the file systems at IDA will not support it.
*/

#include <sys/ioctl.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <linux/fs.h>

#include <unistd.h>
#include <fcntl.h>
#include <stdio.h>
#include <errno.h>
#include <string.h>

int main(int argc, char **argv) {
  int dest_fd, src_fd;
  src_fd = open("a", O_RDONLY);
  dest_fd = open("b", O_WRONLY); /* Needs to exist; not checking this */
  if (ioctl(dest_fd, FICLONE, src_fd) < 0) {
    fprintf(stderr, "error: %s\n", strerror(errno));
    return 1;
  }
  return 0;
}
