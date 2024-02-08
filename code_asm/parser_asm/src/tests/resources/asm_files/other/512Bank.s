	.text
	.syntax unified
	.eabi_attribute	67, "2.09"
	.cpu	cortex-m0
	.eabi_attribute	6, 12
	.eabi_attribute	7, 77
	.eabi_attribute	8, 0
	.eabi_attribute	9, 1
	.eabi_attribute	34, 0
	.eabi_attribute	17, 1
	.eabi_attribute	20, 1
	.eabi_attribute	21, 0
	.eabi_attribute	23, 3
	.eabi_attribute	24, 1
	.eabi_attribute	25, 1
	.eabi_attribute	38, 1
	.eabi_attribute	18, 4
	.eabi_attribute	26, 2
	.eabi_attribute	14, 0
	.file	"512Bank.c"
	.globl	run
	.p2align	1
	.type	run,%function
	.code	16
	.thumb_func
run:
	.fnstart
	.pad	#92
	sub	sp, #92
	@APP
	sub	sp, #508
	@NO_APP
	@APP
	sub	sp, #452
	@NO_APP
	b	.LBB0_1
.LBB0_1:
	b	.LBB0_2
.LBB0_2:
	b	.LBB0_3
.LBB0_3:
	b	.LBB0_4
.LBB0_4:
	b	.LBB0_5
.LBB0_5:
	movs	r0, #80
	str	r0, [sp, #28]
	b	.LBB0_6
.LBB0_6:
	b	.LBB0_7
.LBB0_7:
	movs	r0, #45
	str	r0, [sp, #28]
	b	.LBB0_8
.LBB0_8:
	b	.LBB0_9
.LBB0_9:
	b	.LBB0_10
.LBB0_10:
	movs	r0, #65
	str	r0, [sp, #28]
	b	.LBB0_11
.LBB0_11:
	b	.LBB0_12
.LBB0_12:
	b	.LBB0_13
.LBB0_13:
	movs	r0, #82
	str	r0, [sp, #28]
	b	.LBB0_14
.LBB0_14:
	b	.LBB0_15
.LBB0_15:
	b	.LBB0_16
.LBB0_16:
	movs	r0, #77
	str	r0, [sp, #28]
	b	.LBB0_17
.LBB0_17:
	b	.LBB0_18
.LBB0_18:
	b	.LBB0_19
.LBB0_19:
	movs	r0, #10
	str	r0, [sp, #28]
	b	.LBB0_20
.LBB0_20:
	b	.LBB0_21
.LBB0_21:
	b	.LBB0_22
.LBB0_22:
	b	.LBB0_23
.LBB0_23:
	b	.LBB0_24
.LBB0_24:
	b	.LBB0_25
.LBB0_25:
	b	.LBB0_26
.LBB0_26:
	b	.LBB0_27
.LBB0_27:
	movs	r0, #53
	str	r0, [sp, #28]
	b	.LBB0_28
.LBB0_28:
	b	.LBB0_29
.LBB0_29:
	movs	r0, #49
	str	r0, [sp, #28]
	b	.LBB0_30
.LBB0_30:
	b	.LBB0_31
.LBB0_31:
	b	.LBB0_32
.LBB0_32:
	movs	r0, #50
	str	r0, [sp, #28]
	b	.LBB0_33
.LBB0_33:
	b	.LBB0_34
.LBB0_34:
	b	.LBB0_35
.LBB0_35:
	movs	r0, #66
	str	r0, [sp, #28]
	b	.LBB0_36
.LBB0_36:
	b	.LBB0_37
.LBB0_37:
	b	.LBB0_38
.LBB0_38:
	movs	r0, #97
	str	r0, [sp, #28]
	b	.LBB0_39
.LBB0_39:
	b	.LBB0_40
.LBB0_40:
	b	.LBB0_41
.LBB0_41:
	movs	r0, #110
	str	r0, [sp, #28]
	b	.LBB0_42
.LBB0_42:
	b	.LBB0_43
.LBB0_43:
	b	.LBB0_44
.LBB0_44:
	movs	r0, #107
	str	r0, [sp, #28]
	b	.LBB0_45
.LBB0_45:
	b	.LBB0_46
.LBB0_46:
	movs	r0, #0
	str	r0, [sp, #4]
	b	.LBB0_47
.LBB0_47:
	ldr	r0, [sp, #4]
	cmp	r0, #4
	bgt	.LBB0_52
	b	.LBB0_48
.LBB0_48:
	b	.LBB0_49
.LBB0_49:
	movs	r0, #33
	str	r0, [sp, #28]
	b	.LBB0_50
.LBB0_50:
	b	.LBB0_51
.LBB0_51:
	ldr	r0, [sp, #4]
	adds	r0, r0, #1
	str	r0, [sp, #4]
	b	.LBB0_47
.LBB0_52:
	b	.LBB0_53
.LBB0_53:
	movs	r0, #10
	str	r0, [sp, #28]
	b	.LBB0_54
.LBB0_54:
	movs	r0, #10
	str	r0, [sp]
	b	.LBB0_55
.LBB0_55:
	b	.LBB0_56
.LBB0_56:
	b	.LBB0_57
.LBB0_57:
	b	.LBB0_58
.LBB0_58:
	b	.LBB0_59
.LBB0_59:
	movs	r0, #120
	str	r0, [sp, #28]
	b	.LBB0_60
.LBB0_60:
	b	.LBB0_61
.LBB0_61:
	movs	r0, #61
	str	r0, [sp, #28]
	b	.LBB0_62
.LBB0_62:
	b	.LBB0_63
.LBB0_63:
	b	.LBB0_64
.LBB0_64:
	movs	r0, #49
	str	r0, [sp, #28]
	b	.LBB0_65
.LBB0_65:
	b	.LBB0_66
.LBB0_66:
	b	.LBB0_67
.LBB0_67:
	movs	r0, #48
	str	r0, [sp, #28]
	b	.LBB0_68
.LBB0_68:
	b	.LBB0_69
.LBB0_69:
	b	.LBB0_70
.LBB0_70:
	movs	r0, #10
	str	r0, [sp, #28]
	b	.LBB0_71
.LBB0_71:
	b	.LBB0_72
.LBB0_72:
	ldr	r0, [sp]
	cmp	r0, #6
	blt	.LBB0_132
	b	.LBB0_73
.LBB0_73:
	b	.LBB0_74
.LBB0_74:
	b	.LBB0_75
.LBB0_75:
	b	.LBB0_76
.LBB0_76:
	b	.LBB0_77
.LBB0_77:
	b	.LBB0_78
.LBB0_78:
	b	.LBB0_79
.LBB0_79:
	b	.LBB0_80
.LBB0_80:
	b	.LBB0_81
.LBB0_81:
	b	.LBB0_82
.LBB0_82:
	b	.LBB0_83
.LBB0_83:
	b	.LBB0_84
.LBB0_84:
	b	.LBB0_85
.LBB0_85:
	b	.LBB0_86
.LBB0_86:
	b	.LBB0_87
.LBB0_87:
	b	.LBB0_88
.LBB0_88:
	movs	r0, #71
	str	r0, [sp, #28]
	b	.LBB0_89
.LBB0_89:
	b	.LBB0_90
.LBB0_90:
	movs	r0, #114
	str	r0, [sp, #28]
	b	.LBB0_91
.LBB0_91:
	b	.LBB0_92
.LBB0_92:
	b	.LBB0_93
.LBB0_93:
	movs	r0, #101
	str	r0, [sp, #28]
	b	.LBB0_94
.LBB0_94:
	b	.LBB0_95
.LBB0_95:
	b	.LBB0_96
.LBB0_96:
	movs	r0, #97
	str	r0, [sp, #28]
	b	.LBB0_97
.LBB0_97:
	b	.LBB0_98
.LBB0_98:
	b	.LBB0_99
.LBB0_99:
	movs	r0, #116
	str	r0, [sp, #28]
	b	.LBB0_100
.LBB0_100:
	b	.LBB0_101
.LBB0_101:
	b	.LBB0_102
.LBB0_102:
	movs	r0, #101
	str	r0, [sp, #28]
	b	.LBB0_103
.LBB0_103:
	b	.LBB0_104
.LBB0_104:
	b	.LBB0_105
.LBB0_105:
	movs	r0, #114
	str	r0, [sp, #28]
	b	.LBB0_106
.LBB0_106:
	b	.LBB0_107
.LBB0_107:
	b	.LBB0_108
.LBB0_108:
	movs	r0, #32
	str	r0, [sp, #28]
	b	.LBB0_109
.LBB0_109:
	b	.LBB0_110
.LBB0_110:
	b	.LBB0_111
.LBB0_111:
	movs	r0, #116
	str	r0, [sp, #28]
	b	.LBB0_112
.LBB0_112:
	b	.LBB0_113
.LBB0_113:
	b	.LBB0_114
.LBB0_114:
	movs	r0, #104
	str	r0, [sp, #28]
	b	.LBB0_115
.LBB0_115:
	b	.LBB0_116
.LBB0_116:
	b	.LBB0_117
.LBB0_117:
	movs	r0, #97
	str	r0, [sp, #28]
	b	.LBB0_118
.LBB0_118:
	b	.LBB0_119
.LBB0_119:
	b	.LBB0_120
.LBB0_120:
	movs	r0, #110
	str	r0, [sp, #28]
	b	.LBB0_121
.LBB0_121:
	b	.LBB0_122
.LBB0_122:
	b	.LBB0_123
.LBB0_123:
	movs	r0, #32
	str	r0, [sp, #28]
	b	.LBB0_124
.LBB0_124:
	b	.LBB0_125
.LBB0_125:
	b	.LBB0_126
.LBB0_126:
	movs	r0, #53
	str	r0, [sp, #28]
	b	.LBB0_127
.LBB0_127:
	b	.LBB0_128
.LBB0_128:
	b	.LBB0_129
.LBB0_129:
	movs	r0, #10
	str	r0, [sp, #28]
	b	.LBB0_130
.LBB0_130:
	b	.LBB0_131
.LBB0_131:
	b	.LBB0_235
.LBB0_132:
	b	.LBB0_133
.LBB0_133:
	b	.LBB0_134
.LBB0_134:
	b	.LBB0_135
.LBB0_135:
	b	.LBB0_136
.LBB0_136:
	b	.LBB0_137
.LBB0_137:
	b	.LBB0_138
.LBB0_138:
	b	.LBB0_139
.LBB0_139:
	b	.LBB0_140
.LBB0_140:
	b	.LBB0_141
.LBB0_141:
	b	.LBB0_142
.LBB0_142:
	b	.LBB0_143
.LBB0_143:
	b	.LBB0_144
.LBB0_144:
	b	.LBB0_145
.LBB0_145:
	b	.LBB0_146
.LBB0_146:
	b	.LBB0_147
.LBB0_147:
	b	.LBB0_148
.LBB0_148:
	b	.LBB0_149
.LBB0_149:
	b	.LBB0_150
.LBB0_150:
	b	.LBB0_151
.LBB0_151:
	b	.LBB0_152
.LBB0_152:
	b	.LBB0_153
.LBB0_153:
	b	.LBB0_154
.LBB0_154:
	b	.LBB0_155
.LBB0_155:
	b	.LBB0_156
.LBB0_156:
	b	.LBB0_157
.LBB0_157:
	b	.LBB0_158
.LBB0_158:
	movs	r0, #76
	str	r0, [sp, #28]
	b	.LBB0_159
.LBB0_159:
	b	.LBB0_160
.LBB0_160:
	movs	r0, #101
	str	r0, [sp, #28]
	b	.LBB0_161
.LBB0_161:
	b	.LBB0_162
.LBB0_162:
	b	.LBB0_163
.LBB0_163:
	movs	r0, #115
	str	r0, [sp, #28]
	b	.LBB0_164
.LBB0_164:
	b	.LBB0_165
.LBB0_165:
	b	.LBB0_166
.LBB0_166:
	movs	r0, #115
	str	r0, [sp, #28]
	b	.LBB0_167
.LBB0_167:
	b	.LBB0_168
.LBB0_168:
	b	.LBB0_169
.LBB0_169:
	movs	r0, #101
	str	r0, [sp, #28]
	b	.LBB0_170
.LBB0_170:
	b	.LBB0_171
.LBB0_171:
	b	.LBB0_172
.LBB0_172:
	movs	r0, #114
	str	r0, [sp, #28]
	b	.LBB0_173
.LBB0_173:
	b	.LBB0_174
.LBB0_174:
	b	.LBB0_175
.LBB0_175:
	movs	r0, #32
	str	r0, [sp, #28]
	b	.LBB0_176
.LBB0_176:
	b	.LBB0_177
.LBB0_177:
	b	.LBB0_178
.LBB0_178:
	movs	r0, #116
	str	r0, [sp, #28]
	b	.LBB0_179
.LBB0_179:
	b	.LBB0_180
.LBB0_180:
	b	.LBB0_181
.LBB0_181:
	movs	r0, #104
	str	r0, [sp, #28]
	b	.LBB0_182
.LBB0_182:
	b	.LBB0_183
.LBB0_183:
	b	.LBB0_184
.LBB0_184:
	movs	r0, #97
	str	r0, [sp, #28]
	b	.LBB0_185
.LBB0_185:
	b	.LBB0_186
.LBB0_186:
	b	.LBB0_187
.LBB0_187:
	movs	r0, #110
	str	r0, [sp, #28]
	b	.LBB0_188
.LBB0_188:
	b	.LBB0_189
.LBB0_189:
	b	.LBB0_190
.LBB0_190:
	movs	r0, #32
	str	r0, [sp, #28]
	b	.LBB0_191
.LBB0_191:
	b	.LBB0_192
.LBB0_192:
	b	.LBB0_193
.LBB0_193:
	movs	r0, #111
	str	r0, [sp, #28]
	b	.LBB0_194
.LBB0_194:
	b	.LBB0_195
.LBB0_195:
	b	.LBB0_196
.LBB0_196:
	movs	r0, #114
	str	r0, [sp, #28]
	b	.LBB0_197
.LBB0_197:
	b	.LBB0_198
.LBB0_198:
	b	.LBB0_199
.LBB0_199:
	movs	r0, #32
	str	r0, [sp, #28]
	b	.LBB0_200
.LBB0_200:
	b	.LBB0_201
.LBB0_201:
	b	.LBB0_202
.LBB0_202:
	movs	r0, #101
	str	r0, [sp, #28]
	b	.LBB0_203
.LBB0_203:
	b	.LBB0_204
.LBB0_204:
	b	.LBB0_205
.LBB0_205:
	movs	r0, #113
	str	r0, [sp, #28]
	b	.LBB0_206
.LBB0_206:
	b	.LBB0_207
.LBB0_207:
	b	.LBB0_208
.LBB0_208:
	movs	r0, #117
	str	r0, [sp, #28]
	b	.LBB0_209
.LBB0_209:
	b	.LBB0_210
.LBB0_210:
	b	.LBB0_211
.LBB0_211:
	movs	r0, #97
	str	r0, [sp, #28]
	b	.LBB0_212
.LBB0_212:
	b	.LBB0_213
.LBB0_213:
	b	.LBB0_214
.LBB0_214:
	movs	r0, #108
	str	r0, [sp, #28]
	b	.LBB0_215
.LBB0_215:
	b	.LBB0_216
.LBB0_216:
	b	.LBB0_217
.LBB0_217:
	movs	r0, #32
	str	r0, [sp, #28]
	b	.LBB0_218
.LBB0_218:
	b	.LBB0_219
.LBB0_219:
	b	.LBB0_220
.LBB0_220:
	movs	r0, #116
	str	r0, [sp, #28]
	b	.LBB0_221
.LBB0_221:
	b	.LBB0_222
.LBB0_222:
	b	.LBB0_223
.LBB0_223:
	movs	r0, #111
	str	r0, [sp, #28]
	b	.LBB0_224
.LBB0_224:
	b	.LBB0_225
.LBB0_225:
	b	.LBB0_226
.LBB0_226:
	movs	r0, #32
	str	r0, [sp, #28]
	b	.LBB0_227
.LBB0_227:
	b	.LBB0_228
.LBB0_228:
	b	.LBB0_229
.LBB0_229:
	movs	r0, #53
	str	r0, [sp, #28]
	b	.LBB0_230
.LBB0_230:
	b	.LBB0_231
.LBB0_231:
	b	.LBB0_232
.LBB0_232:
	movs	r0, #10
	str	r0, [sp, #28]
	b	.LBB0_233
.LBB0_233:
	b	.LBB0_234
.LBB0_234:
	b	.LBB0_235
.LBB0_235:
	b	.LBB0_236
.LBB0_236:
	b	.LBB0_237
.LBB0_237:
	b	.LBB0_237
.Lfunc_end0:
	.size	run, .Lfunc_end0-run
	.cantunwind
	.fnend

	.ident	"Ubuntu clang version 14.0.0-1ubuntu1.1"
	.section	".note.GNU-stack","",%progbits
	.addrsig
	.eabi_attribute	30, 6
