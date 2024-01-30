/* TODO: Detect if FICLONE is available; else use a generic function */
void copy_files()
{
  int dest_fd, src_fd;
  src_fd = open("a", O_RDONLY);
  dest_fd = open("b", O_WRONLY); /* Needs to exist; not checking this */
  if (ioctl(dest_fd, FICLONE, src_fd) < 0) {
    fprintf(stderr, "error: %s\n", strerror(errno));
    return;
  }
}
