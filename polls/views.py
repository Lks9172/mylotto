from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.utils import timezone
from django.views.generic import DetailView, ListView

from polls.models import Question


# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:3]
#     return render(request, 'polls/index.html', {'latest_question_list': latest_question_list})
#

# def detail(request, pk):
#     q = get_object_or_404(Question, pk = pk)
#     return render(request, 'polls/detail.html', {'question' : q})
#
# def results(request, pk): #question_id를 파라미터로 받는다.
#     return HttpResponse("You're looking at the results of question %s" % pk)

class IndexView(ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list' #파라미터를 무슨 이름으로 넘길 것인가?

    def get_queryset(self): # 메소드 오버라이딩
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(DetailView):
    # 어느 모델과 연결해서 어느 템플릿으로 넘겨 줄지 정의한다.
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(DetailView):
    model = Question
    template_name = 'polls/results.html'

def vote(request, pk): #POST를 처리할 수 있도록 작성한다.
    question = get_object_or_404(Question, pk = pk)
    try:
        # POST form에서 'choice' name 값을 갖는 input의 value 값을 가져온다.
        selected_choice = question.choice_set.get(pk = request.POST['choice'])
    except:

        return render(request, 'polls/detail.html', {
            'question' : question,
            'error_message' : "You didn't select a choice"
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return redirect('polls:results', pk = question.id)


def get_queryset(self):
    return Question.objects.filter(
        pub_date__lte=timezone.now()
    ).order_by('-pub_date')[:5]