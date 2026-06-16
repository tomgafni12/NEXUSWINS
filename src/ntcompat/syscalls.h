#ifndef SYSCALLS_H
#define SYSCALLS_H

#include <linux/types.h>

/*
 * NexusWins NTCompat
 * Windows NT Syscall Table
 * Maps Windows NT syscalls to Linux equivalents
 */

/* NT Status codes */
#define STATUS_SUCCESS              0x00000000
#define STATUS_UNSUCCESSFUL         0xC0000001
#define STATUS_NOT_IMPLEMENTED      0xC0000002
#define STATUS_ACCESS_DENIED        0xC0000022
#define STATUS_INVALID_HANDLE       0xC0000008

/* Core NT syscalls we need to fake */
#define NtCreateFile            0x0055
#define NtReadFile              0x0006
#define NtWriteFile             0x0008
#define NtClose                 0x000F
#define NtAllocateVirtualMemory 0x0018
#define NtFreeVirtualMemory     0x001E
#define NtCreateThread          0x004E
#define NtTerminateProcess      0x002C
#define NtQuerySystemInformation 0x0036

/* Syscall translation function */
long nt_syscall_handler(unsigned int syscall_id, 
                        unsigned long arg1,
                        unsigned long arg2,
                        unsigned long arg3,
                        unsigned long arg4);

#endif /* SYSCALLS_H */