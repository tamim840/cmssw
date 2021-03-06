import FWCore.ParameterSet.Config as cms

m1 = cms.EDProducer("prod")
m2 = cms.EDProducer("prod")
m3 = cms.EDProducer("prod")
m4 = cms.EDProducer("prod")
m5 = cms.EDProducer("prod")
m6 = cms.EDProducer("prod")
m7 = cms.EDProducer("prod")
m8 = cms.EDProducer("prod")
m9 = cms.EDProducer("prod")
m10 = cms.EDProducer("prod")
m11 = cms.EDProducer("prod")
m12 = cms.EDProducer("prod")
m13 = cms.EDProducer("prod")
m14 = cms.EDProducer("prod")
m15 = cms.EDProducer("prod")
m16 = cms.EDProducer("prod")
m17 = cms.EDProducer("prod")
m18 = cms.EDProducer("prod")
m19 = cms.EDProducer("prod")
m20 = cms.EDProducer("prod")
m21 = cms.EDProducer("prod")
m22 = cms.EDProducer("prod")
m23 = cms.EDProducer("prod")
m24 = cms.EDProducer("prod")
m25 = cms.EDProducer("prod")
m26 = cms.EDProducer("prod")
m27 = cms.EDProducer("prod")
m28 = cms.EDProducer("prod")
m29 = cms.EDProducer("prod")
m30 = cms.EDProducer("prod")

p1 = cms.Path(m3+m4)
t1 = cms.Task(m11, m12)
t2 = cms.Task(m13, m14)
t3 = cms.Task(m15, m16)
t4 = cms.Task(m17, m18)
s1 = cms.Sequence(m5+m6, t3, t4)
s2 = cms.Sequence(s1)
p2 = cms.Path(s2, t1, t2)
e1 = cms.EndPath(m7+m8)
t5 = cms.Task(m19, m20)
t6 = cms.Task(m21, m22)
t7 = cms.Task(m23, m24)
t8 = cms.Task(m25, m26)
s3 = cms.Sequence(m9+m10, t5, t6)
s4 = cms.Sequence(s3)
e2 = cms.EndPath(s4, t7, t8)
t9 = cms.Task(m27, m28)

f1 = cms.EDFilter("filt")
f2 = cms.EDFilter("filt")
f3 = cms.EDFilter("filt")
f4 = cms.EDFilter("filt")
f5 = cms.EDFilter("filt")
f6 = cms.EDFilter("filt")
f7 = cms.EDFilter("filt")
f8 = cms.EDFilter("filt")
f9 = cms.EDFilter("filt")
f10 = cms.EDFilter("filt")
f11 = cms.EDFilter("filt")
f12 = cms.EDFilter("filt")
f13 = cms.EDFilter("filt")
f14 = cms.EDFilter("filt")
f15 = cms.EDFilter("filt")
f16 = cms.EDFilter("filt")
f17 = cms.EDFilter("filt")
f18 = cms.EDFilter("filt")
f19 = cms.EDFilter("filt")
f20 = cms.EDFilter("filt")
f21 = cms.EDFilter("filt")
f22 = cms.EDFilter("filt")
f23 = cms.EDFilter("filt")
f24 = cms.EDFilter("filt")
f25 = cms.EDFilter("filt")
f26 = cms.EDFilter("filt")
f27 = cms.EDFilter("filt")
f28 = cms.EDFilter("filt")
f29 = cms.EDFilter("filt")
f30 = cms.EDFilter("filt")

pf1 = cms.Path(f3+f4)
tf1 = cms.Task(f11, f12)
tf2 = cms.Task(f13, f14)
tf3 = cms.Task(f15, f16)
tf4 = cms.Task(f17, f18)
sf1 = cms.Sequence(f5+f6, tf3, tf4)
sf2 = cms.Sequence(sf1)
pf2 = cms.Path(sf2, tf1, tf2)
ef1 = cms.EndPath(f7+f8)
tf5 = cms.Task(f19, f20)
tf6 = cms.Task(f21, f22)
tf7 = cms.Task(f23, f24)
tf8 = cms.Task(f25, f26)
sf3 = cms.Sequence(f9+f10, tf5, tf6)
sf4 = cms.Sequence(sf3)
ef2 = cms.EndPath(sf4, tf7, tf8)
tf9 = cms.Task(f27, f28)

a1 = cms.EDAnalyzer("an")
a2 = cms.EDAnalyzer("an")
a3 = cms.EDAnalyzer("an")
a4 = cms.EDAnalyzer("an")
a5 = cms.EDAnalyzer("an")
a6 = cms.EDAnalyzer("an")
a7 = cms.EDAnalyzer("an")
a8 = cms.EDAnalyzer("an")
a9 = cms.EDAnalyzer("an")
a10 = cms.EDAnalyzer("an")

pa1 = cms.Path(a3+a4)
sa1 = cms.Sequence(a5+a6)
sa2 = cms.Sequence(sa1)
pa2 = cms.Path(sa2)
ea1 = cms.EndPath(a7+a8)
sa3 = cms.Sequence(a9+a10)
sa4 = cms.Sequence(sa3)
ea2 = cms.EndPath(sa4)

o1 = cms.OutputModule("out")
o2 = cms.OutputModule("out")
o7 = cms.OutputModule("out")
o8 = cms.OutputModule("out")
o9 = cms.OutputModule("out")
o10 = cms.OutputModule("out")

eo1 = cms.EndPath(o7+o8)
so3 = cms.Sequence(o9+o10)
so4 = cms.Sequence(so3)
eo2 = cms.EndPath(so4)

ess1 = cms.ESSource("ess")  # labeled case
ess2 = cms.ESSource("ess2") # unlabeled case
ess3 = cms.ESSource("ess")
ess4 = cms.ESSource("ess4")
ess11 = cms.ESSource("ess")
ess12 = cms.ESSource("ess12")
ess13 = cms.ESSource("ess")
ess14 = cms.ESSource("ess14")
ess15 = cms.ESSource("ess")
ess16 = cms.ESSource("ess16")
ess17 = cms.ESSource("ess")
ess18 = cms.ESSource("ess18")
ess19 = cms.ESSource("ess")
ess20 = cms.ESSource("ess20")
ess21 = cms.ESSource("ess")
ess22 = cms.ESSource("ess22")
ess23 = cms.ESSource("ess")
ess24 = cms.ESSource("ess24")
ess25 = cms.ESSource("ess")
ess26 = cms.ESSource("ess26")
ess27 = cms.ESSource("ess")
ess28 = cms.ESSource("ess28")

tess10 = cms.Task(ess3, ess4)
tess1 = cms.Task(ess11, ess12)
tess2 = cms.Task(ess13, ess14)
tess3 = cms.Task(ess15, ess16)
tess4 = cms.Task(ess17, ess18)
sess1 = cms.Sequence(tess3, tess4)
sess2 = cms.Sequence(sess1)
pess2 = cms.Path(sess2, tess1, tess2)
tess5 = cms.Task(ess19, ess20)
tess6 = cms.Task(ess21, ess22)
tess7 = cms.Task(ess23, ess24)
tess8 = cms.Task(ess25, ess26)
sess3 = cms.Sequence(tess5, tess6)
sess4 = cms.Sequence(sess3)
eess2 = cms.EndPath(sess4, tess7, tess8)

esp1 = cms.ESProducer("esp")
esp2 = cms.ESProducer("esp2")
esp3 = cms.ESProducer("esp")
esp4 = cms.ESProducer("esp4")
esp11 = cms.ESProducer("esp")
esp12 = cms.ESProducer("esp12")
esp13 = cms.ESProducer("esp")
esp14 = cms.ESProducer("esp14")
esp15 = cms.ESProducer("esp")
esp16 = cms.ESProducer("esp16")
esp17 = cms.ESProducer("esp")
esp18 = cms.ESProducer("esp18")
esp19 = cms.ESProducer("esp")
esp20 = cms.ESProducer("esp20")
esp21 = cms.ESProducer("esp")
esp22 = cms.ESProducer("esp22")
esp23 = cms.ESProducer("esp")
esp24 = cms.ESProducer("esp24")
esp25 = cms.ESProducer("esp")
esp26 = cms.ESProducer("esp26")
esp27 = cms.ESProducer("esp")
esp28 = cms.ESProducer("esp28")

tesp10 = cms.Task(esp3, esp4)
tesp1 = cms.Task(esp11, esp12)
tesp2 = cms.Task(esp13, esp14)
tesp3 = cms.Task(esp15, esp16)
tesp4 = cms.Task(esp17, esp18)
sesp1 = cms.Sequence(tesp3, tesp4)
sesp2 = cms.Sequence(sesp1)
pesp2 = cms.Path(sesp2, tesp1, tesp2)
tesp5 = cms.Task(esp19, esp20)
tesp6 = cms.Task(esp21, esp22)
tesp7 = cms.Task(esp23, esp24)
tesp8 = cms.Task(esp25, esp26)
sesp3 = cms.Sequence(tesp5, tesp6)
sesp4 = cms.Sequence(sesp3)
eesp2 = cms.EndPath(sesp4, tesp7, tesp8)

serv1 = cms.Service("serv1")
serv2 = cms.Service("serv2")
serv3 = cms.Service("serv3")
serv4 = cms.Service("serv4")
serv11 = cms.Service("serv11")
serv12 = cms.Service("serv12")
serv13 = cms.Service("serv13")
serv14 = cms.Service("serv14")
serv15 = cms.Service("serv15")
serv16 = cms.Service("serv16")
serv17 = cms.Service("serv17")
serv18 = cms.Service("serv18")
serv19 = cms.Service("serv19")
serv20 = cms.Service("serv20")
serv21 = cms.Service("serv21")
serv22 = cms.Service("serv22")
serv23 = cms.Service("serv23")
serv24 = cms.Service("serv24")
serv25 = cms.Service("serv25")
serv26 = cms.Service("serv26")
serv27 = cms.Service("serv27")
serv28 = cms.Service("serv28")

tserv10 = cms.Task(serv3, serv4)
tserv1 = cms.Task(serv11, serv12)
tserv2 = cms.Task(serv13, serv14)
tserv3 = cms.Task(serv15, serv16)
tserv4 = cms.Task(serv17, serv18)
sserv1 = cms.Sequence(tserv3, tserv4)
sserv2 = cms.Sequence(sserv1)
pserv2 = cms.Path(sserv2, tserv1, tserv2)
tserv5 = cms.Task(serv19, serv20)
tserv6 = cms.Task(serv21, serv22)
tserv7 = cms.Task(serv23, serv24)
tserv8 = cms.Task(serv25, serv26)
sserv3 = cms.Sequence(tserv5, tserv6)
sserv4 = cms.Sequence(sserv3)
eserv2 = cms.EndPath(sserv4, tserv7, tserv8)
