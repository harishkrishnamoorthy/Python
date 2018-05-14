# -*- coding: utf-8 -*-
import base64
import datetime
import io
import sys

import dash
from dash.dependencies import Input, Output, State
import dash_core_components as dcc
import dash_html_components as html
import dash_table_experiments as dt

import pandas as pd


import pandas as pd
import numpy as np
import nltk
from nltk.stem.wordnet import WordNetLemmatizer
import en

#Training libraries
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer

reload(sys)
sys.setdefaultencoding('utf-8')

#Training algorigthm
train_text = state_union.raw("2005-GWBush.txt")
custom_sent_tokenizer = PunktSentenceTokenizer(train_text)

# creating a function that will retrive only base verb forms
is_verb = lambda pos: pos == 'VB'


#Single 'should' - past tense
def transform_stmt_single_shd_past(stmt):
    words = nltk.word_tokenize(stmt)
    veb_lst = [word for (word, pos) in nltk.pos_tag(words) if is_verb(pos)]

    if (stmt.find("should not") > -1) and ('be' in veb_lst):
        trnf_pst_stmt = stmt.replace("should not be", "was not")
        return trnf_pst_stmt

    elif (stmt.find("should not") > -1):
        trnf_pst_stmt = stmt.replace("should not", "did not")
        return trnf_pst_stmt

    elif (stmt.find("should") > -1) and (stmt.find("and") > -1) and ('be' not in veb_lst) and (stmt.find("create") > -1):
        trnf_pst_stmt1 = stmt.replace("should "+veb_lst[0], en.verb.past(veb_lst[0].lower()))
        trnf_pst_stmt2 = trnf_pst_stmt1.replace("create", "created")
        return trnf_pst_stmt2

    elif (stmt.find("should") > -1) and ('be' in veb_lst) and (stmt.find("details") > stmt.find("field")):
        trnf_pst_stmt = stmt.replace("should be", "are")
        return trnf_pst_stmt

    elif (stmt.find("should") > -1) and ('be' in veb_lst) and (stmt.find("sections") > -1) and (stmt.find("screen") > -1):
        trnf_pst_stmt = stmt.replace("should be", "was")
        return trnf_pst_stmt

    elif (stmt.find("should") > -1) and ('be' in veb_lst) and (stmt.find("details") > -1):
        trnf_pst_stmt = stmt.replace("should be", "were")
        return trnf_pst_stmt

    elif (stmt.find("should") > -1) and ('be' in veb_lst) and (stmt.find("properties") > -1):
        trnf_pst_stmt = stmt.replace("should be", "were")
        return trnf_pst_stmt

    elif (stmt.find("should") > -1) and ('be' in veb_lst) and (stmt.find("fields") > -1):
        trnf_pst_stmt = stmt.replace("should be", "were")
        return trnf_pst_stmt

    elif (stmt.find("should") > -1) and ('be' in veb_lst) and (stmt.find("sections") > -1):
        trnf_pst_stmt = stmt.replace("should be", "were")
        return trnf_pst_stmt

    elif (stmt.find("should") > -1) and ('be' in veb_lst):
        trnf_pst_stmt = stmt.replace("should be", "was")
        return trnf_pst_stmt

    elif (stmt.find("should") > -1) and ('be' not in veb_lst):
        trnf_pst_stmt = stmt.replace("should "+veb_lst[0], en.verb.past(veb_lst[0].lower()))
        return trnf_pst_stmt

    else:
        return stmt


#Single 'should' - present tense
def transform_stmt_single_shd_present(stmt):
    words = nltk.word_tokenize(stmt)
    veb_lst = [word for (word, pos) in nltk.pos_tag(words) if is_verb(pos)]

    if (stmt.find("should not") > -1) and ('be' in veb_lst) and (stmt.find("fields") > -1):
        trnf_present_stmt = stmt.replace("should not be", "are not")
        return trnf_present_stmt

    elif (stmt.find("should not") > -1) and ('be' in veb_lst):
        trnf_present_stmt = stmt.replace("should not be", "is not")
        return trnf_present_stmt

    elif (stmt.find("should not") > -1):
        trnf_present_stmt = stmt.replace("should not", "does not")
        return trnf_present_stmt

    elif (stmt.find("should") > -1) and (stmt.find("and") > -1) and ('be' not in veb_lst) and (stmt.find("create") > -1):
        trnf_present_stmt1 = stmt.replace("should "+veb_lst[0], en.verb.present(veb_lst[0].lower()))
        trnf_present_stmt2 = trnf_present_stmt1.replace("create", "created")
        return trnf_present_stmt2

    elif (stmt.find("should") > -1) and ('be' in veb_lst) and (stmt.find("details") > stmt.find("field")):
        trnf_present_stmt = stmt.replace("should be", "is")
        return trnf_present_stmt

    elif (stmt.find("should") > -1) and ('be' in veb_lst) and (stmt.find("sections") > -1) and (stmt.find("screen") > -1):
        trnf_present_stmt = stmt.replace("should be", "is")
        return trnf_present_stmt

    elif (stmt.find("should") > -1) and ('be' in veb_lst) and (stmt.find("details") > -1):
        trnf_present_stmt = stmt.replace("should be", "are")
        return trnf_present_stmt

    elif (stmt.find("should") > -1) and ('be' in veb_lst) and (stmt.find("properties") > -1):
        trnf_present_stmt = stmt.replace("should be", "are")
        return trnf_present_stmt

    elif (stmt.find("should") > -1) and ('be' in veb_lst) and (stmt.find("fields") > -1):
        trnf_present_stmt = stmt.replace("should be", "are")
        return trnf_present_stmt

    elif (stmt.find("should") > -1) and ('be' in veb_lst) and (stmt.find("sections") > -1):
        trnf_present_stmt = stmt.replace("should be", "are")
        return trnf_present_stmt

    elif (stmt.find("should") > -1) and ('be' not in veb_lst) and (stmt.find("retrieve") > -1):
        trnf_present_stmt = stmt.replace("should retrieve", "retrieves")
        return trnf_present_stmt

    elif (stmt.find("should") > -1) and ('be' in veb_lst):
        trnf_present_stmt = stmt.replace("should be", "is")
        return trnf_present_stmt

    elif (stmt.find("should") > -1) and ('be' not in veb_lst):
        trnf_present_stmt = stmt.replace("should "+veb_lst[0], en.verb.present(veb_lst[0].lower(), person=3, negate=False))
        return trnf_present_stmt

    else:
        return stmt


#multiple 'should' - present
def transform_stmt_mul_shd_present(stmt):
    temp_pst_collate = ""
    splt_sentence = stmt.split("and")
    for stmt in splt_sentence:
        temp_pst_collate = temp_pst_collate + 'and' + transform_stmt_single_shd_present(stmt)
        #print(temp_pst_collate)
    return temp_pst_collate[3:]



#multiple 'should' - past
def transform_stmt_mul_shd_past(stmt):
    temp_pst_collate = ""
    splt_sentence = stmt.split("and")
    for stmt in splt_sentence:
        temp_pst_collate = temp_pst_collate + 'and' + transform_stmt_single_shd_past(stmt)
        #print(temp_pst_collate)
    return temp_pst_collate[3:]



#process Expected result - convert to present tense
def processExpRes_present(df):
    #verb_lst = []
    all_prsnt_stmt = []
    temp_pst = ""

    for test_case in list(df["test_Step_Expected_result"]):
        stmt_lst = custom_sent_tokenizer.tokenize(test_case)
        try:
            for stmt in stmt_lst:
                words = nltk.word_tokenize(stmt)
                if words.count("should") > 1:
                    temp_pst = temp_pst + '\n' + transform_stmt_mul_shd_present(stmt)
                else:
                    temp_pst = temp_pst + '\n' + transform_stmt_single_shd_present(stmt)

            all_prsnt_stmt.append(temp_pst[1:])
            #print (temp_pst)
            temp_pst = ""

        except Exception as e:
            all_prsnt_stmt.append(test_case)
            print(str(e))
    se = pd.Series(all_prsnt_stmt)
    df['Conv_exptd_prsnt'] = se.values



#process Expected result - convert to past tense
def processExpRes_past(df):
    #verb_lst = []
    all_past_stmt = []
    temp_pst = ""

    for test_case in list(df["test_Step_Expected_result"]):
        stmt_lst = custom_sent_tokenizer.tokenize(test_case)
        try:
            for stmt in stmt_lst:
                words = nltk.word_tokenize(stmt)
                if words.count("should") > 1:
                    temp_pst = temp_pst + '\n' + transform_stmt_mul_shd_past(stmt)
                else:
                    temp_pst = temp_pst + '\n' + transform_stmt_single_shd_past(stmt)

            all_past_stmt.append(temp_pst[1:])
            #print (temp_pst)
            temp_pst = ""

        except Exception as e:
            all_past_stmt.append(test_case)
            print(str(e))
    se = pd.Series(all_past_stmt)
    df['Conv_exptd_past'] = se.values



#process actual result - trim User Info
def processActRes(df):
    trm_act_res = []
    for test_case in list(df["test_step_Actual_result"]):
        try:
            #print (test_case)
            trm_act_res.append(test_case[:test_case.rfind("[")])
        except Exception as e:
            trm_act_res.append(test_case)
            print(str(e))
    ac = pd.Series(trm_act_res)
    df['Converted_Actual'] = ac.values


def generatecompResult(df):
    cmpexpactlst = []
    resulttxt = ''
    for index, row in df.iterrows():
        #print(row["Converted_Expected"] +"----> \n"+  row["Converted_Actual"])

        x_prsnt = row["Conv_exptd_prsnt"].replace(' ', '')
        x1_prsnt = x_prsnt.replace('\n', '') #replacing new lines
        x2_prsnt = x1_prsnt.replace('\r', '')#replacing returns
        x3_prsnt = x2_prsnt.replace('"','')#replacing "
        x4_prsnt = x3_prsnt.replace('.','')#replacing .

        x_past = row["Conv_exptd_past"].replace(' ', '')
        x1_past = x_past.replace('\n', '') #replacing new lines
        x2_past = x1_past.replace('\r', '')#replacing returns
        x3_past = x2_past.replace('"','')#replacing "
        x4_past = x3_past.replace('.','')#replacing .

        y = row["Converted_Actual"].replace(' ', '')
        y1 = y.replace('\n', '') #replacing new lines
        y2 = y1.replace('\r', '') #replacing returnss
        y3 = y2.replace('"','')#replacing "
        y4 = y3.replace('.','')#replacing .

        if (x4_prsnt == y4) or (x4_past == y4):
            resulttxt = 'Approved'
        elif (x4_prsnt in y4) or (x4_past in y4):
            #y2.contains(x2):
            resulttxt = 'Approved'
        else:
            resulttxt = 'Verify'
        cmpexpactlst.append(resulttxt)
    res = pd.Series(cmpexpactlst)
    df["Compare_result"] = res.values

def generateStepList(df):
    keys,vals = df.sort_values('TEST_ID').values.T
    ukeys, index = np.unique(keys, True)
    arrays = np.split(vals, index[1:])
    df2 = pd.DataFrame({'TEST_ID':ukeys, 'Steps to Verify':[list(a) for a in arrays]})
    return df2


def generateSummary(df):
    cnts = pd.DataFrame(df.TEST_ID.value_counts().reset_index())
    cnts.columns = ["TEST_ID", "Total Steps"]
    df1 = df.loc[df['Compare_result'] == "Approved"]
    appcnts = pd.DataFrame(df1.TEST_ID.value_counts().reset_index())
    appcnts.columns = ["TEST_ID", "Approved"]
    df2 = df.loc[df['Compare_result'] == "Verify"]
    vrfycnts = pd.DataFrame(df2.TEST_ID.value_counts().reset_index())
    vrfycnts.columns = ["TEST_ID", "Verify"]
    xxx = generateStepList(df2[['TEST_ID','test_step_name']])
    df10 = cnts.merge(appcnts, on='TEST_ID', how='left').merge(vrfycnts, on='TEST_ID', how='left').merge(xxx, on='TEST_ID', how='left')
    df11 = df10.fillna(0)
    df11[['Approved','Verify']] = df11[['Approved','Verify']].astype(int)
    df11['Action'] = df11.apply(lambda x: 'Approve' if x["Verify"]==0 else 'Verify', axis=1)
    final_sum_df = df11[["TEST_ID", "Action", "Total Steps", "Approved", "Verify", "Steps to Verify"]]
    return final_sum_df



app = dash.Dash()

app.scripts.config.serve_locally = True
app.css.append_css({'external_url': 'https://stackpath.bootstrapcdn.com/bootstrap/4.1.1/css/bootstrap.min.css'})
app.layout = html.Div([
    html.Div(
        html.Nav([
            html.A(['Test Result Review'], className="nav-brand mb-0 h4 text-white"),
            #html.A(['Home'], href = '#', className="nav-link mr-auto text-white"),
            html.A(['Help'], href = '#', className="nav-link text-white")
        ], className="navbar navbar-dark bg-dark")
    ),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Div([
        html.Div([
            html.H1("Test Results Review"),
            html.P("Upload excel or CSV file(s) to get started ..", className="lead"),
                dcc.Upload(
                    id='upload-data',
                    children=html.Div([
                        '',
                        html.Button("Upload", id='upload-data', className="btn btn-dark")
                    ]),
                    # Allow multiple files to be uploaded
                    multiple=True
                )
        ], className="starter-template")
    ], className ="cover-container d-flex w-100 h-100 p-3 mx-auto flex-column text-center"),
    html.Div(id='output-data-upload'),
    html.Div(dt.DataTable(rows=[{}]), style={'display': 'none'})
])

def parse_contents(contents, filename, date):
    content_type, content_string = contents.split(',')
    print("-1")
    decoded = base64.b64decode(content_string)
    try:
        print("0")
        if 'csv' in filename:
            # Assume that the user uploaded a CSV file
            print("1")
            df = pd.read_csv(io.StringIO(decoded.decode('utf-8')))

        elif 'xls' in filename:
            print("2")
            # Assume that the user uploaded an excel file
            df = pd.read_excel(io.BytesIO(decoded))


        processExpRes_present(df)
        processExpRes_past(df)
        processActRes(df)
        generatecompResult(df)
        summaryStats_df= generateSummary(df)
        time = datetime.datetime.now().strftime("%m_%d_%Y_%H%M%S")

        new_filename = 'Results saved at:  C:\\Result_{}.xlsx'.format(time)
        old_filename = filename[:filename.find('.')]
        with pd.ExcelWriter ('C:\\Results./{}_Result_{}.xlsx'.format(old_filename, time)) as writer:
            summaryStats_df.to_excel(writer, sheet_name = 'Summary', engine='xlsxwriter', encoding='utf-8', index=False)
            df.to_excel(writer, sheet_name = 'Data', engine='xlsxwriter', encoding='utf-8', index=False)
            writer.save()


    except Exception as e:
        print(e)
        return html.Div([
            'There was an error processing this file.'
        ])

    return html.Div([
        html.H5("Input filename: " + filename),
        #html.H6("Processing started at: " + str(datetime.datetime.fromtimestamp(date))),
        html.H6 (new_filename),
        # Use the DataTable prototype component:
        # github.com/plotly/dash-table-experiments
        dt.DataTable(
            rows=summaryStats_df.to_dict('records'),
            columns = (["TEST_ID", "Action", "Total Steps", "Approved", "Verify", "Steps to Verify"]),
            filterable=True),

        html.Hr(),  # horizontal line
    ])

@app.callback(Output('output-data-upload', 'children'),
              [Input('upload-data', 'contents')],
              [State('upload-data', 'filename'),
               State('upload-data', 'last_modified')])
def update_output(list_of_contents, list_of_names, list_of_dates):
    if list_of_contents is not None:
        children = [
            parse_contents(c, n, d) for c, n, d in
            zip(list_of_contents, list_of_names, list_of_dates)]
        return children

if __name__ == '__main__':
    app.run_server(debug=True)
