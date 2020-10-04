from datetime import datetime
from xerparser.model.classes.calendar import Calendar
from xerparser.model.classes.wbs import WBS


class Task:
    # obj_list = []

    def __init__(self, params):
        # Unique ID generated by the system.
        self.task_id = int(params[0]) if params[0] else None
        # project to which the activity belongs referenced by system generated unique id
        self.proj_id = int(params[1]) if params[1] else None
        # wbs element activity assigned to referenced by system unique id
        self.wbs_id = int(params[2]) if params[2] else None
        # calendar assigned to activity referenced by system unique id
        self.clndr_id = int(params[3]) if params[3] else None
        # The physical percent complete can either be user entered or calculated from the activity's weighted steps.
        #  There is a project setting specifying this.
        self.phys_complete_pct = float(params[4]) if params[4] else None
        # Indicates that the primary resource has sent feedback notes about this activity which have not been
        # reviewed yet.
        self.rev_fdbk_flag = bool(params[5]) if params[5] else None
        # The estimation weight for the activity, used for top-down estimation. Top-down estimation weights are used
        # to calculate the proportion of units that each activity receives in relation to the other activities within
        #  the same WBS. Top-down estimation distributes estimated units in a top-down manner to activities using the
        #  WBS hierarchy.
        self.est_wt = float(params[6]) if params[6] else None
        # Indicates that the planned labor and nonlabor units for the activity will not be modified by top-down
        # estimation.
        self.lock_plan_flag = bool(params[7]) if params[7] else None
        # Identifies whether the actual and remaining cost for the expense are computed automatically using the
        # planned cost and the activity's schedule percent complete.  If this option is selected,
        # the actual/remaining cost are automatically updated when project actuals are applied.  This assumes the
        # expenses are made according to plan.
        self.auto_compute_act_flag = bool(params[8]) if params[8] else None
        # The activity percent complete type is one of ""Duration"", ""Units"", or ""Physical"". The percent complete
        #  type controls whether the Activity % Complete is tied to the Duration % Complete, the Units % Complete,
        # or the Physical % Complete for the activity. Set the percent complete type to ""Duration"" for activities
        # which are duration driven, for example, administration tasks and training classes.  Set the percent
        # complete type to ""Physical"" for activities which are work-product driven, for example, creating a
        # document or a product. Set the percent complete type to ""Units"" for activities which are work effort
        # driven, for example, providing a consulting service.
        self.complete_pct_type = params[9].strip()
        # The type of activity, either  'Task Dependent', 'Resource Dependent', 'Level of Effort', 'Start Milestone'
        # or 'Finish Milestone'.   A Task Dependent activity is scheduled using the activity's calendar rather than
        # the calendars of the assigned resources.  A Resource Dependent activity is scheduled using the calendars of
        #  the assigned resources.  This type is used when several resources are assigned to the activity,
        # but they may work separately.  A Start/Finish Milestone is a zero-duration activity, marking a significant
        # start/end of project event. A Level of Effort activity has a duration which is determined by its dependent
        # activities. Administration-type activities are typically level of effort.
        self.task_type = params[10].strip()
        # The duration type of the activity. One of ""Fixed Units per Time"", ""Fixed Duration"", or ""Fixed Units"".
        #   For Fixed Units per Time activities, the resource units per time are constant when the activity duration
        # or units are changed.  This type is used when an activity has fixed resources with fixed productivity
        # output per time period.  For Fixed Duration activities, the activity duration is constant as the units or
        # resource units per time are changed. This type is used when the activity is to be completed within a fixed
        # time period regardless of the resources assigned.  For Fixed Units activities, the activity units are
        # constant when the duration or resource units per time are changed. This type is used when the total amount
        # of work is fixed, and increasing the resources can decrease the activity duration.
        self.duration_type = params[11].strip()
        # The current status of the activity, either Not Started, In Progress, or Completed.
        self.status_code = params[12].strip()
        # A short ID which uniquely identifies the activity within the project.
        self.task_code = params[13].strip()
        # The name of the activity. The activity name does not have to be unique.
        self.task_name = params[14].strip()
        # Resource ID Name
        self.rsrc_id = int(params[15]) if params[15] else None
        # The amount of time the wbs can be delayed before delaying the project finish date. Total float can be
        # computed as Late Start - Early Start or as Late Finish - Early Finish; this option can be set when running
        # the project scheduler.
        self.total_float_hr_cnt = float(params[16].strip()) if params[16] else None
        # The amount of time the activity can be delayed before delaying the start date of any successor activity.
        self.free_float_hr_cnt = float(params[17]) if params[17] else None
        # Remaining duration is the total working time from the activity remaining start date to the remaining finish
        #  date. The remaining working time is computed using the activity's calendar. Before the activity is
        # started, the remaining duration is the same as the Original Duration. After the activity is completed the
        # remaining duration is zero.
        self.remain_drtn_hr_cnt = float(params[18].strip()) if params[18] else 0
        # The total actual labor units for all child activities
        self.act_work_qty = float(params[19]) if params[19] else None
        # The remaining units for all labor resources assigned to the activity. The remaining units reflects the work
        #  remaining to be done for the activity. Before the activity is started, the remaining units are the same as
        #  the planned units. After the activity is completed, the remaining units are zero.
        self.remain_work_qty = float(params[20]) if params[20] else None
        # The planned units for all labor resources assigned to the activity.
        self.target_work_qty = float(params[21]) if params[21] else None
        # Original Duration is the planned working time for the resource assignment on the activity,
        # from the resource's planned start date to the planned finish date. The planned working time is computed
        # using the calendar determined by the Activity Type. Resource Dependent activities use the resource's
        # calendar; other activity types use the activity's calendar. This is the duration that Timesheets users
        # follow and the schedule variance is measured against.
        self.target_drtn_hr_cnt = float(params[22].strip()) if params[18] else 0.0
        # The planned units for all nonlabor resources assigned to the activity.
        self.target_equip_qty = float(params[23]) if params[23] else None
        # The actual units for all nonlabor resources assigned to the activities under the WBS.
        self.act_equip_qty = float(params[24]) if params[24] else None
        # The remaining units for all nonlabor resources assigned to the activity. The remaining units reflects the
        # work remaining to be done for the activity.  Before the activity is started, the remaining units are the
        # same as the planned units. After the activity is completed, the remaining units are zero.
        self.remain_equip_qty = float(params[25]) if params[25] else None
        # The constraint date for the activity, if the activity has a constraint. The activity's constraint type
        # determines whether this is a start date or finish date.  Activity constraints are used by the project
        # scheduler.
        self.cstr_date = datetime.strptime(params[26], '%Y-%m-%d %H:%M') if params[26] else None
        # The date on which the activity is actually started.
        self.act_start_date = datetime.strptime(params[27], '%Y-%m-%d %H:%M') if params[27] else None
        # The date on which the activity is actually finished.
        self.act_end_date = datetime.strptime(params[28], '%Y-%m-%d %H:%M') if params[28] else None
        # the activity late start date
        self.late_start_date = datetime.strptime(params[29], '%Y-%m-%d %H:%M') if params[29] else None
        # The latest possible date the activity must finish without delaying the project finish date. This date is
        # computed by the project scheduler based on network logic, schedule constraints, and resource availability.
        self.late_end_date = datetime.strptime(params[30], '%Y-%m-%d %H:%M') if params[30] else None
        # The date the activity is expected to be finished according to the progress made on the activity's work
        # products. The expected finish date is entered manually by people familiar with progress of the activity's
        # work products.
        self.expect_end_date = datetime.strptime(params[31], '%Y-%m-%d %H:%M') if params[31] else None
        # The earliest possible date the remaining work for the activity can begin. This date is computed by the
        # project scheduler based on network logic, schedule constraints, and resource availability.
        self.early_start_date = datetime.strptime(params[32], '%Y-%m-%d %H:%M') if params[32] else None
        # The earliest possible date the activity can finish. This date is computed by the project scheduler based on
        #  network logic, schedule constraints, and resource availability.
        self.early_end_date = datetime.strptime(params[33], '%Y-%m-%d %H:%M') if params[33] else None
        # The date the remaining work for the activity is scheduled to begin. This date is computed by the project
        # scheduler but can be updated manually by the project manager.  Before the activity is started,
        # the remaining start date is the same as the planned start date.  This is the start date that Timesheets
        # users follow.
        self.restart_date = datetime.strptime(params[34], '%Y-%m-%d %H:%M') if params[34] else None
        # The date the remaining work for the activity is scheduled to finish. This date is computed by the project
        # scheduler but can be updated manually by the project manager. Before the activity is started, the remaining
        #  finish date is the same as the planned finish date.  This is the finish date that Timesheets users follow.
        self.reend_date = datetime.strptime(params[35], '%Y-%m-%d %H:%M') if params[35] else None
        # The date the activity is scheduled to begin. This date is computed by the project scheduler but can be
        # updated manually by the project manager. This date is not changed by the project scheduler after the
        # activity has been started.
        self.target_start_date = datetime.strptime(params[36], '%Y-%m-%d %H:%M') if params[36] else None
        # The date the activity is scheduled to finish. This date is computed by the project scheduler but can be
        # updated manually by the project manager.  This date is not changed by the project scheduler after the
        # activity has been started.
        self.target_end_date = datetime.strptime(params[37], '%Y-%m-%d %H:%M') if params[37] else None
        # Remaining late start date is calculated by the scheduler.
        self.rem_late_start_date = datetime.strptime(params[38], '%Y-%m-%d %H:%M') if params[38] else None
        # Remaining late end date is calculated by the scheduler.
        self.rem_late_end_date = datetime.strptime(params[39], '%Y-%m-%d %H:%M') if params[39] else None
        # The type of constraint applied to the activity start or finish date. Activity constraints are used by the
        # project scheduler.  Start date constraints are 'Start On', 'Start On or Before', 'Start On or After' and
        # 'Mandatory Start'.  Finish date constraints are 'Finish On', 'Finish On or Before', 'Finish On or After'
        # and 'Mandatory Finish'.  Another type of constraint, 'As Late as Possible', schedules the activity as late
        # as possible based on the available free float.
        self.cstr_type = params[40].strip()
        self.priority_type = params[41].strip()
        # The date progress is suspended on an activity.
        self.suspend_date = datetime.strptime(params[42], '%Y-%m-%d %H:%M') if params[42] else None
        # The date progress is resumed on an activity.
        self.resume_date = datetime.strptime(params[43], '%Y-%m-%d %H:%M') if params[43] else None
        self.float_path = params[44].strip()
        # This field is computed by the project scheduler and identifies the order in which the activities were
        # processed within the float path.
        self.float_path_order = params[45].strip()
        self.guid = params[46].strip()
        self.tmpl_guid = params[47].strip()
        # The second constraint date for the activity, if the activity has a constraint.
        self.cstr_date2 = datetime.strptime(params[48], '%Y-%m-%d %H:%M') if params[48] else None
        # The second type of constraint applied to the activity start or finish date.
        self.cstr_type2 = params[49].strip()
        self.driving_path_flag = bool(params[50]) if params[50] else None
        # The actual this period units for all labor resources assigned to the activity.
        self.act_this_per_work_qty = float(params[51]) if params[51] else None
        # The actual this period units for all nonlabor resources assigned to the activity.
        self.act_this_per_equip_qty = float(params[52]) if params[52] else None
        # The External Early Start date is the date the external relationship was scheduled to finish.  This date may
        #  be used to calculate the start date of the current activity during scheduling.  This field is populated on
        #  import when an external relationship is lost.
        self.external_early_start_date = datetime.strptime(params[53], '%Y-%m-%d %H:%M') if params[48] else None
        self.external_late_end_date = datetime.strptime(params[54], '%Y-%m-%d %H:%M') if params[48] else None

        self.create_date = params[55].strip()
        self.update_date = params[56].strip()
        self.create_user = params[57].strip()
        self.update_user = params[58].strip()
        self.location_id = params[59].strip()
        self.calendar = Calendar.find_by_id(self.clndr_id)
        self.wbs = WBS.find_by_id(int(self.wbs_id) if self.wbs_id else None)
        # Task.obj_list.append(self)

    @property
    def id(self):
        return self.task_id

    @property
    def float(self):
        if self.total_float_hr_cnt:
            tf = float(self.total_float_hr_cnt)/8.0
        else:
            return None
        return tf

    @property
    def duration(self):
        dur = None
        if self.target_drtn_hr_cnt:
            dur = float(self.target_drtn_hr_cnt) / float(self.calendar.day_hr_cnt)
        else:
            dur =0.0
        return dur

    @property
    def constraints(self):
        return {"ConstraintType": self.cstr_type,
                "ConstrintDate": self.cstr_date}

    @property
    def start_date(self):
        if self.act_start_date:
            return self.act_start_date
        else:
            return self.target_start_date

    @property
    def end_date(self):
        if self.act_end_date:
            return self.act_end_date
        else:
            return self.target_start_date

    def __repr__(self):
        return self.task_code