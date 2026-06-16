# NTCompat — Windows NT Kernel Compatibility Layer

The most ambitious part of NexusWins.
Goal: mask the Linux kernel as Windows NT at ring 0.

## What needs to be implemented
- [ ] Windows NT kernel structures (KPCR, KPRCB, PEB, TEB)
- [ ] NT syscall table translation
- [ ] Windows registry at kernel level
- [ ] CPUID spoofing to hide hypervisor
- [ ] Windows kernel driver loader (.sys files)
- [ ] NT memory layout emulation

## References
- ReactOS source (ntoskrnl)
- Wine ntdll implementation
- Windows NT internals documentation

## Warning
This is genuinely one of the hardest things
in systems programming. It will take time.