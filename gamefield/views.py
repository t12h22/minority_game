import random
from django.shortcuts import render, redirect
from .models import Question, Answer

def game_view(request):
    if request.method == 'POST':
        selected_choice = request.POST.get('choice')
        question_id = request.POST.get('question_id')
        question = Question.objects.get(id=question_id)
        Answer.objects.create(question=question, choice=selected_choice)
        return redirect('game_view')

    # ランダムな2択の問題を取得
    questions = Question.objects.all()
    question = random.choice(questions)

    # 各選択肢の回答数を取得
    choices = ['Choice A', 'Choice B']
    choice_counts = [question.answer_set.filter(choice=choice).count() for choice in choices]

    context = {
        'question': question,
        'choices': choices,
        'choice_counts': choice_counts,
    }
    return render(request, 'game.html', context)
