#ifndef NTSTRUCTS_H
#define NTSTRUCTS_H

#include <linux/types.h>

/* 
 * NexusWins NTCompat
 * Windows NT Kernel Structure Definitions
 * "There are nexuses, causal relationships that cannot be separated"
 */

/* Thread Environment Block - every Windows thread has one */
typedef struct _TEB {
    void* ExceptionList;
    void* StackBase;
    void* StackLimit;
    void* SubSystemTib;
    void* FiberData;
    void* ArbitraryUserPointer;
    struct _TEB* Self;
} TEB;

/* Process Environment Block - every Windows process has one */
typedef struct _PEB {
    __u8  InheritedAddressSpace;
    __u8  ReadImageFileExecOptions;
    __u8  BeingDebugged;
    __u8  Spare;
    void* Mutant;
    void* ImageBaseAddress;
    void* Ldr;
} PEB;

#endif /* NTSTRUCTS_H */