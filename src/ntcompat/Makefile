# NexusWins NTCompat - Kernel Module Makefile

obj-m += ntcompat.o
ntcompat-objs := ntcompat.o

KDIR := /lib/modules/$(shell uname -r)/build

all:
	make -C $(KDIR) M=$(PWD) modules

clean:
	make -C $(KDIR) M=$(PWD) clean

install:
	sudo insmod ntcompat.ko

uninstall:
	sudo rmmod ntcompat