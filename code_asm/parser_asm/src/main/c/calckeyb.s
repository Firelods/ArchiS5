	.cpu arm7tdmi
	.eabi_attribute 20, 1
	.eabi_attribute 21, 1
	.eabi_attribute 23, 3
	.eabi_attribute 24, 1
	.eabi_attribute 25, 1
	.eabi_attribute 26, 1
	.eabi_attribute 30, 6
	.eabi_attribute 34, 0
	.eabi_attribute 18, 4
	.file	"calckeyb.c"
	.text
	.align	2
	.global	run
	.arch armv4t
	.syntax unified
	.arm
	.fpu softvfp
	.type	run, %function
run:
	@ Function supports interworking.
	@ args = 0, pretend = 0, frame = 112
	@ frame_needed = 1, uses_anonymous_args = 0
	@ link register save eliminated.
	push	{r4, r5, fp}
	add	fp, sp, #8
	sub	sp, sp, #116
	.syntax divided
@ 7 "calckeyb.c" 1
	sub sp, #508
@ 0 "" 2
@ 7 "calckeyb.c" 1
	sub sp, #452
@ 0 "" 2
	.arm
	.syntax unified
	mov	r3, #65
	str	r3, [fp, #-104]
	mov	r3, #61
	str	r3, [fp, #-104]
	mov	r3, #0
	str	r3, [fp, #-16]
.L8:
	nop
.L2:
	ldr	r3, [fp, #-80]
	cmp	r3, #0
	beq	.L2
	ldr	r3, [fp, #-76]
	str	r3, [fp, #-24]
	ldr	r3, [fp, #-24]
	cmp	r3, #10
	beq	.L42
	ldr	r3, [fp, #-24]
	cmp	r3, #47
	ble	.L43
	ldr	r3, [fp, #-24]
	cmp	r3, #57
	bgt	.L43
	ldr	r3, [fp, #-24]
	str	r3, [fp, #-104]
	ldr	r2, [fp, #-16]
	mov	r3, r2
	lsl	r3, r3, #2
	add	r3, r3, r2
	lsl	r3, r3, #1
	str	r3, [fp, #-16]
	ldr	r3, [fp, #-24]
	sub	r3, r3, #48
	ldr	r2, [fp, #-16]
	add	r3, r2, r3
	str	r3, [fp, #-16]
	b	.L8
.L43:
	nop
	b	.L8
.L42:
	nop
	ldr	r3, [fp, #-16]
	str	r3, [fp, #-28]
	mov	r3, #10
	str	r3, [fp, #-104]
	mov	r3, #66
	str	r3, [fp, #-104]
	mov	r3, #61
	str	r3, [fp, #-104]
	mov	r3, #0
	str	r3, [fp, #-20]
.L15:
	nop
.L9:
	ldr	r3, [fp, #-80]
	cmp	r3, #0
	beq	.L9
	ldr	r3, [fp, #-76]
	str	r3, [fp, #-32]
	ldr	r3, [fp, #-32]
	cmp	r3, #10
	beq	.L44
	ldr	r3, [fp, #-32]
	cmp	r3, #47
	ble	.L45
	ldr	r3, [fp, #-32]
	cmp	r3, #57
	bgt	.L45
	ldr	r3, [fp, #-32]
	str	r3, [fp, #-104]
	ldr	r2, [fp, #-20]
	mov	r3, r2
	lsl	r3, r3, #2
	add	r3, r3, r2
	lsl	r3, r3, #1
	str	r3, [fp, #-20]
	ldr	r3, [fp, #-32]
	sub	r3, r3, #48
	ldr	r2, [fp, #-20]
	add	r3, r2, r3
	str	r3, [fp, #-20]
	b	.L15
.L45:
	nop
	b	.L15
.L44:
	nop
	ldr	r3, [fp, #-20]
	str	r3, [fp, #-36]
	mov	r3, #10
	str	r3, [fp, #-104]
	mov	r3, #43
	str	r3, [fp, #-104]
	mov	r3, #45
	str	r3, [fp, #-104]
	mov	r3, #42
	str	r3, [fp, #-104]
	mov	r3, #47
	str	r3, [fp, #-104]
	mov	r3, #37
	str	r3, [fp, #-104]
	mov	r3, #38
	str	r3, [fp, #-104]
	mov	r3, #124
	str	r3, [fp, #-104]
	mov	r3, #94
	str	r3, [fp, #-104]
.L16:
	nop
.L17:
	ldr	r3, [fp, #-80]
	cmp	r3, #0
	beq	.L17
	ldr	r3, [fp, #-76]
	str	r3, [fp, #-40]
	ldr	r3, [fp, #-40]
	cmp	r3, #124
	beq	.L18
	ldr	r3, [fp, #-40]
	cmp	r3, #124
	bgt	.L16
	ldr	r3, [fp, #-40]
	cmp	r3, #47
	bgt	.L20
	ldr	r3, [fp, #-40]
	cmp	r3, #37
	blt	.L16
	ldr	r3, [fp, #-40]
	sub	r3, r3, #37
	cmp	r3, #10
	ldrls	pc, [pc, r3, asl #2]
	b	.L16
.L22:
	.word	.L27
	.word	.L26
	.word	.L16
	.word	.L16
	.word	.L16
	.word	.L25
	.word	.L24
	.word	.L16
	.word	.L23
	.word	.L16
	.word	.L21
.L20:
	ldr	r3, [fp, #-40]
	cmp	r3, #94
	beq	.L28
	b	.L19
.L24:
	ldr	r2, [fp, #-28]
	ldr	r3, [fp, #-36]
	add	r3, r2, r3
	str	r3, [fp, #-100]
	b	.L29
.L23:
	ldr	r2, [fp, #-28]
	ldr	r3, [fp, #-36]
	sub	r3, r2, r3
	str	r3, [fp, #-100]
	b	.L29
.L25:
	ldr	r3, [fp, #-28]
	ldr	r2, [fp, #-36]
	mul	r3, r2, r3
	str	r3, [fp, #-100]
	b	.L29
.L21:
	ldr	r3, [fp, #-28]
	ldr	r2, [fp, #-36]
	.syntax divided
@ 37 "calckeyb.c" 1
	movs r4, r3
movs r5, r2
@ 0 "" 2
	.arm
	.syntax unified
	ldr	r3, [fp, #-56]
	str	r3, [fp, #-100]
	b	.L29
.L27:
	ldr	r3, [fp, #-28]
	ldr	r2, [fp, #-36]
	.syntax divided
@ 40 "calckeyb.c" 1
	movs r4, r3
movs r5, r2
@ 0 "" 2
	.arm
	.syntax unified
	ldr	r3, [fp, #-52]
	str	r3, [fp, #-100]
	b	.L29
.L26:
	ldr	r2, [fp, #-28]
	ldr	r3, [fp, #-36]
	and	r3, r3, r2
	str	r3, [fp, #-100]
	b	.L29
.L18:
	ldr	r2, [fp, #-28]
	ldr	r3, [fp, #-36]
	orr	r3, r2, r3
	str	r3, [fp, #-100]
	b	.L29
.L28:
	ldr	r2, [fp, #-28]
	ldr	r3, [fp, #-36]
	eor	r3, r3, r2
	str	r3, [fp, #-100]
	b	.L29
.L19:
	b	.L16
.L29:
	mov	r3, #10
	str	r3, [fp, #-104]
	mov	r3, #82
	str	r3, [fp, #-104]
	mov	r3, #61
	str	r3, [fp, #-104]
	ldr	r3, [fp, #-60]
	str	r3, [fp, #-108]
	ldr	r3, [fp, #-108]
	cmp	r3, #0
	bne	.L30
	mov	r3, #48
	str	r3, [fp, #-104]
	b	.L31
.L30:
	ldr	r3, [fp, #-100]
	cmp	r3, #0
	bge	.L32
	mov	r3, #45
	str	r3, [fp, #-104]
	ldr	r3, [fp, #-100]
	rsb	r3, r3, #0
	str	r3, [fp, #-100]
	ldr	r3, [fp, #-60]
	str	r3, [fp, #-108]
.L32:
	mov	r3, #0
	str	r3, [fp, #-112]
	mov	r3, #0
	str	r3, [fp, #-116]
	b	.L33
.L37:
	ldr	r3, [fp, #-108]
	and	r3, r3, #15
	str	r3, [fp, #-120]
	ldr	r3, [fp, #-108]
	lsr	r3, r3, #4
	str	r3, [fp, #-108]
	ldr	r3, [fp, #-112]
	cmp	r3, #0
	bne	.L34
	ldr	r3, [fp, #-120]
	cmp	r3, #0
	beq	.L46
	mov	r3, #1
	str	r3, [fp, #-112]
.L34:
	ldr	r3, [fp, #-120]
	add	r3, r3, #48
	str	r3, [fp, #-104]
	b	.L36
.L46:
	nop
.L36:
	ldr	r3, [fp, #-116]
	add	r3, r3, #1
	str	r3, [fp, #-116]
.L33:
	ldr	r3, [fp, #-116]
	cmp	r3, #7
	bls	.L37
.L31:
	nop
.L38:
	ldr	r3, [fp, #-80]
	cmp	r3, #0
	beq	.L38
	mov	r3, #1
	str	r3, [fp, #-88]
.L39:
	b	.L39
	.size	run, .-run
	.ident	"GCC: (15:10.3-2021.07-4) 10.3.1 20210621 (release)"
