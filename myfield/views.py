from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import TestField


#
# def dataform(request):
#     return render(request,"field.html",{})



def data(request):
    # form = TestField(request.POST or None)
    form = TestField
    if request.method == 'POST':
        form = form(request.POST)
        if form.is_valid():
            a = form.cleaned_data.get("first_interest")
            b = form.cleaned_data.get("first_principal")
            c = form.cleaned_data.get("other_rent")
            d = form.cleaned_data.get("other_tax")
            e = form.cleaned_data.get("other_interest")
            f = form.cleaned_data.get("other_principal")
            g = form.cleaned_data.get("save_acc")
            h = form.cleaned_data.get("fixed_deposit")
            i = form.cleaned_data.get("kvp_ivp")
            j = form.cleaned_data.get("nsc_1")
            k = form.cleaned_data.get("nsc_2")
            l = form.cleaned_data.get("nsc_3")
            m1 = form.cleaned_data.get("fd_1")
            m2 = form.cleaned_data.get("fd_2")
            m3 = form.cleaned_data.get("fd_3")
            n = form.cleaned_data.get("b_d")
            o = form.cleaned_data.get("i_property")
            p = form.cleaned_data.get("ppf")
            q = form.cleaned_data.get("pension")
            r = form.cleaned_data.get("lic")
            s = form.cleaned_data.get("fdr")
            t = form.cleaned_data.get("fees")
            u = form.cleaned_data.get("mf_uti")
            v = form.cleaned_data.get("n_pension")
            w = form.cleaned_data.get("edu_loan")
            x = form.cleaned_data.get("m_parent")
            y = form.cleaned_data.get("m_you")
            z = form.cleaned_data.get("d11")
            aa = form.cleaned_data.get("d12")
            bb = form.cleaned_data.get("d21")
            cc = form.cleaned_data.get("d22")
            dd = form.cleaned_data.get("d31")
            ee = form.cleaned_data.get("d32")
            ff1 = form.cleaned_data.get("d_1")
            ff2 = form.cleaned_data.get("d_2")
            ff3 = form.cleaned_data.get("d_3")

            gg = form.cleaned_data.get("section_1")
            hh = form.cleaned_data.get("section_2")
            ii = form.cleaned_data.get("other_deduct")
            jj = form.cleaned_data.get("interest_due")
            kk = form.cleaned_data.get("p_repayment")

            ll = form.cleaned_data.get("ifsc")
            mm = form.cleaned_data.get("acc")

            tt = form.cleaned_data.get("time")

            from_email = settings.EMAIL_HOST_USER
            to_email = [from_email, 'vamagithub@gmail.com']

            contact_message = "HOUSE PROPERTY\n" \
                              "First House: \n" \
                              "Interest: %s \t \n" \
                              "Principal: %s \t \n " \
                              "Other Income" \
                              "%s \t %s \t %s \t %s \t %s " \
                              "\t%s \t%s \t%s \t%s \t%s \t%s \t%s \t%s \t%s" \
                              " \t%s \t%s \t%s \t%s \t%s \t%s \t%s \t%s \t%s " \
                              "\t%s \t%s \t%s \t%s " \
                              "\t %s\t %s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t" % (
                                  a, b, c, d, e, f, g, h, i, j, k, l, n, o, p, q, r, s, t, u, v, w, x, y, z, aa, bb, cc, dd,
                                  ee,
                                  gg, hh, ii, m1, m2, m3, ff1, ff2, ff3, jj, kk, ll, mm, tt)

            send_mail('Fields Data from a customer',
                      contact_message,
                      from_email,
                      to_email,
                      fail_silently=False)  # SEE THIS MAKE IT TRUE IT DOESNOT WORK
            # return HttpResponseRedirect('thanks')
            # return render(request, "field.html", {"form": form, })
            return render(request,"pay.html",{"form": form, })

    else:
        form = TestField()

    return render(request, "field.html", {"form": form, })

