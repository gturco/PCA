
base_name = "chromosome_SEQID.TISSUE.mr.meth.MTYPE.hypo"
def main(base_name):
    mtypes = ["CHG","CHH","CG"]
    tissues = ['vascular','nonvascular', 'root','shoot']
    names = []
    for n in range(1,11):
        name = base_name.replace("SEQID",str(n))
        for tissue in tissues:
            tname = name.replace("TISSUE",tissue)
        for mtype in mtypes:
            mname = tname.replace("MTYPE",mtype)
            print mname

main(base_name)





